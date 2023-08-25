#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>
#include <WiFiClientSecure.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <ArduinoJson.h>
#include <StreamUtils.h>
//#include "vars.h" <- Template for variables
#include "hiddenVars.h"

#define SEALEVELPRESSURE_HPA (1013.25)

// Making definitions
Adafruit_BME280 bme;

float inTemp;
float inHum;
float pressure;
float exTemp;
String exCond;
float exRain;
float exWind;
float exFeelTemp;

void setup() {
  Serial.begin(9600);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialise BME280 sensor
  if (!bme.begin(0x76)) {
    Serial.println("Could not find a valid BME280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  getInternalData();
  Serial.print(String(inTemp));
  getExternalData();
  delay(1000);
  postData();
  delay(10 * 60 * 1000); // 10 minutes
}

void getInternalData() {  
  // Read BME280 sensor values
  inTemp = bme.readTemperature();
  inHum = bme.readHumidity();
  pressure = bme.readPressure() / 100.0;
}

void getExternalData() {

  String response;
  exCond = "";
  const char* exCondTemp;
  // Create an instance of the WiFiClient and HTTPClient class
  WiFiClient client;
  HTTPClient http;

  delay(1000);  
  // Connect to WeatherAPI.com to get current temperature
  String urlString = "http://api.weatherapi.com/v1/current.json?key=" + String(apiKey) + "&q=" + String(postCode) + "&aqi=no";
  http.useHTTP10(true);
  http.begin(client, urlString);
  http.GET();

  // Parse response
  DynamicJsonDocument doc(2048);
  deserializeJson(doc, http.getStream());

  // Read values
  exTemp = doc["current"]["temp_c"];
  exCondTemp = doc["current"]["condition"]["text"];

  // Roundabout way to remove spaces, as it was giving issues when posting
  String tmp = String(exCondTemp);
  for (size_t i = 0; i < tmp.length(); i++) {
    if (tmp.charAt(i) != ' ') {
      exCond += tmp.charAt(i);
    }
    // Late addition, added hyphen for easier reading
    else {
      exCond += "-";
    }
  }
  exRain = doc["current"]["precip_mm"];
  exWind = doc["current"]["wind_mph"];
  exFeelTemp = doc["current"]["feelslike_c"];
  
  Serial.println("Current Temp: " + String(exTemp) + "C" + String(exCond));
  client.stop();
}

void postData() {
  // Define another instance
  WiFiClientSecure client;
  // Setting insecure just in case, wasn't sure if Caddy was a problem when posting
  client.setInsecure();
// Create the payload in x-www-form-urlencoded format
  String payload = "api_key=" + String(api_key) +
                     "&inTemp=" + String(inTemp) +
                     "&inHum=" + String(inHum) +
                     "&exTemp=" + String(exTemp) +
                     "&exCond=" + String(exCond) +
                     "&exRain=" + String(exRain) +
                     "&exWind=" + String(exWind) +
                     "&exFeelTemp=" + String(exFeelTemp);

    // Connect to the server
    if (client.connect(serverAddress, serverPort)) {
      // Make the HTTP POST request
      client.print(String("POST ") + postEndpoint + " HTTP/1.1\r\n" +
                   "Host: " + serverAddress + "\r\n" +
                   "Content-Type: application/x-www-form-urlencoded\r\n" +
                   "Content-Length: " + payload.length() + "\r\n" +
                   "Connection: close\r\n\r\n" +
                   payload);

      // Read and display the HTTP response
      while (client.connected()) {
        String line = client.readStringUntil('\n');
        if (line == "\r") {
          break;
        }
      }
      while (client.available()) {
        Serial.write(client.read());
      }
      client.stop();
    } else {
      Serial.println("Error connecting to server");
    }
}
