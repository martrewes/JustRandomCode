/*
 *    SPDX-FileCopyrightText: 2013 Sebastian Kügler <sebas@kde.org>
 *    SPDX-FileCopyrightText: 2014 Kai Uwe Broulik <kde@privat.broulik.de>
 *    SPDX-FileCopyrightText: 2020 Ismael Asensio <isma.af@gmail.com>
 *
 *    SPDX-License-Identifier: LGPL-2.0-or-later
 */
pragma ComponentBehavior: Bound

import QtQuick
import org.kde.plasma.plasmoid
import org.kde.plasma.core as PlasmaCore
import org.kde.plasma.plasma5support as Plasma5Support
import org.kde.plasma.private.mpris as Mpris
import org.kde.kirigami as Kirigami

PlasmoidItem {
    id: root

    switchWidth: Kirigami.Units.gridUnit * 14
        switchHeight: Kirigami.Units.gridUnit * 10

            readonly property int volumePercentStep: 5

            // BEGIN model properties
            readonly property string mprisTrack: mpris2Model.currentPlayer?.track ?? ""
            readonly property string mprisArtist: mpris2Model.currentPlayer?.artist ?? ""
            readonly property string mprisAlbum: mpris2Model.currentPlayer?.album ?? ""
            readonly property string albumArt: mpris2Model.currentPlayer?.artUrl ?? ""
            readonly property string identity: mpris2Model.currentPlayer?.identity ?? ""
            readonly property bool canControl: mpris2Model.currentPlayer?.canControl ?? false
            readonly property bool canGoPrevious: mpris2Model.currentPlayer?.canGoPrevious ?? false
            readonly property bool canGoNext: mpris2Model.currentPlayer?.canGoNext ?? false
            readonly property bool canPlay: mpris2Model.currentPlayer?.canPlay ?? false
            readonly property bool canPause: mpris2Model.currentPlayer?.canPause ?? false
            readonly property bool canStop: mpris2Model.currentPlayer?.canStop ?? false
            readonly property int playbackStatus: mpris2Model.currentPlayer?.playbackStatus ?? 0
            readonly property bool isPlaying: root.playbackStatus === Mpris.PlaybackStatus.Playing
            readonly property bool canRaise: mpris2Model.currentPlayer?.canRaise ?? false
            readonly property bool canQuit: mpris2Model.currentPlayer?.canQuit ?? false
            readonly property int shuffle: mpris2Model.currentPlayer?.shuffle ?? 0
            readonly property int loopStatus: mpris2Model.currentPlayer?.loopStatus ?? 0
            readonly property real playbackRate: mpris2Model.currentPlayer?.rate ?? 1.0
            readonly property real minimumPlaybackRate: mpris2Model.currentPlayer?.minimumRate ?? 1.0
            readonly property real maximumPlaybackRate: mpris2Model.currentPlayer?.maximumRate ?? 1.0

            // Custom extended metadata properties populated by gdbus (with mpris2Model fallback)
            property string dbusTrack: ""
            property string dbusArtist: ""
            property string dbusAlbum: ""
            property string dbusLength: ""
            property string trackNo: ""
            property string trackDate: ""

            readonly property string track: dbusTrack || mprisTrack
            readonly property string artist: dbusArtist || mprisArtist
            readonly property string album: dbusAlbum || mprisAlbum

            readonly property string customAlbum: {
                return root.album ? " .:. " + root.album : "";
            }

            readonly property string trackLength: {
                if (dbusLength) {
                    return dbusLength;
                }
                const rawLength = mpris2Model.currentPlayer?.length ?? 0;
                if (rawLength <= 0) {
                    return "";
                }
                const secs = Math.floor(rawLength / 1000000);
                const formatted = new Date(secs * 1000).toISOString().substring(11, 19);
                return formatted.startsWith("00:") ? " (" + formatted.substring(3, 8) + ")" : " (" + formatted + ")";
            }

            // Zero-quote gdbus query for full MPRIS Metadata dictionary
            readonly property string metadataCmd: "sh -c 'for s in $(busctl --user list --no-legend | grep -o ^org.mpris.MediaPlayer2.[^[:space:]]*); do st=$(gdbus call --session -d $s -o /org/mpris/MediaPlayer2 -m org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player PlaybackStatus 2>/dev/null); case $st in *Playing*) exec gdbus call --session -d $s -o /org/mpris/MediaPlayer2 -m org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player Metadata 2>/dev/null;; esac; fb=$s; done; test -n $fb && exec gdbus call --session -d $fb -o /org/mpris/MediaPlayer2 -m org.freedesktop.DBus.Properties.Get org.mpris.MediaPlayer2.Player Metadata 2>/dev/null'"

            Plasma5Support.DataSource {
                id: extraMetadataSource
                engine: "executable"
                connectedSources: []

                onNewData: (sourceName, data) => {
                    const stdout = (data["stdout"] || "").trim();
                    disconnectSource(sourceName);

                    if (!stdout) {
                        root.dbusTrack = "";
                        root.dbusArtist = "";
                        root.dbusAlbum = "";
                        root.dbusLength = "";
                        root.trackNo = "";
                        root.trackDate = "";
                        return;
                    }

                    // Extract string values after 'key': ... 'value'
                    const getStr = (key) => {
                        const idx = stdout.indexOf("'" + key + "':");
                        if (idx === -1) return "";
                        const rest = stdout.slice(idx + key.length + 3);
                        const qMatch = rest.match(/^\s*(?:[a-z0-9]+\s+)?(['"])/);
                        if (!qMatch) return "";
                        const [, quote] = qMatch;
                        const valRe = new RegExp("^\\s*(?:[a-z0-9]+\\s+)?" + quote + "((?:\\\\" + quote + "|[^" + quote + "])*)" + quote);
                        const m = rest.match(valRe);
                        if (!m) return "";
                        const [, val] = m;
                        return val.replace(new RegExp("\\\\" + quote, "g"), quote);
                    };

                    root.dbusTrack = getStr("xesam:title");
                    root.dbusAlbum = getStr("xesam:album");

                    // Extract artist array between [ and ]
                    //const artistArrMatch = stdout.match(/'xesam:artist':[^\[]*\[([^\]]*)\]/);
                    
                    // Extract artist array between [ and ] (supporting both ' and " items)
                    const artistArrMatch = stdout.match(/'xesam:artist':[^\[]*\[([^\]]*)\]/);
                    if (artistArrMatch) {
                        const [, rawList] = artistArrMatch;
                        const artists = [];
                        const re = /(['"])((?:\\.|(?!\1).)*)\1/g;
                        let item;
                        while ((item = re.exec(rawList)) !== null) {
                            const [, quote, artistName] = item;
                            artists.push(artistName.replace(new RegExp("\\\\" + quote, "g"), quote));
                        }
                        root.dbusArtist = artists.join(", ");
                    } else {
                        root.dbusArtist = "";
                    }

                    // Length: digits after 'mpris:length':
                    //const lenMatch = stdout.match(/'mpris:length':[^0-9]*(\d+)/);
                    const lenMatch = stdout.match(/'mpris:length':[^a-z0-9]*(?:[a-z]+\d*\s+)?(\d+)/);
                    if (lenMatch) {
                        const [, rawLen] = lenMatch;
                        const secs = Math.floor(parseInt(rawLen, 10) / 1000000);
                        const formatted = new Date(secs * 1000).toISOString().substring(11, 19);
                        root.dbusLength = formatted.startsWith("00:") ? " (" + formatted.substring(3, 8) + ")" : " (" + formatted + ")";
                    } else {
                        root.dbusLength = "";
                    }

                    // Track Number: digits after 'xesam:trackNumber':
                    const trackMatch = stdout.match(/'xesam:trackNumber':[^0-9]*(\d+)/);
                    let num = 0;
                    if (trackMatch) {
                        const [, rawNum] = trackMatch;
                        num = parseInt(rawNum, 10);
                    }
                    root.trackNo = num > 0 ? num + ". " : "";

                    // Year: 4 digits after 'year': or 'xesam:contentCreated':
                    const yearMatch = stdout.match(/'year':[^0-9]*(\d{4})/);
                    const createdMatch = stdout.match(/'xesam:contentCreated':[^0-9]*(\d{4})/);
                    let yearStr = "";
                    if (yearMatch) {
                        const [, y] = yearMatch;
                        yearStr = y;
                    } else if (createdMatch) {
                        const [, c] = createdMatch;
                        yearStr = c;
                    }
                    root.trackDate = yearStr ? " [" + yearStr + "]" : "";
                }

            }

            function refreshExtraMetadata(): void {
                if (root.mprisTrack.length === 0) {
                    root.dbusTrack = "";
                    root.dbusArtist = "";
                    root.dbusAlbum = "";
                    root.dbusLength = "";
                    root.trackNo = "";
                    root.trackDate = "";
                    return;
                }
                extraMetadataSource.disconnectSource(root.metadataCmd);
                extraMetadataSource.connectSource(root.metadataCmd);
            }

            onMprisTrackChanged: refreshExtraMetadata()
            onIdentityChanged: refreshExtraMetadata()
            // END model properties

            Plasmoid.icon: switch (root.playbackStatus) {
                case Mpris.PlaybackStatus.Playing:
                    return "media-playback-playing-symbolic";
                case Mpris.PlaybackStatus.Paused:
                    return "media-playback-paused-symbolic";
                default:
                    return "media-playback-stopped-symbolic";
            }
            Plasmoid.status: PlasmaCore.Types.PassiveStatus
            toolTipMainText: root.playbackStatus > Mpris.PlaybackStatus.Stopped ? root.track : i18n("No media playing")
            toolTipSubText: switch (root.playbackStatus) {
                case Mpris.PlaybackStatus.Playing:
                    return root.artist ? i18nc("@info:tooltip %1 is a musical artist and %2 is an app name", "by %1 (%2)\n%3\n", root.artist, root.identity, root.customAlbum)
                    : i18nc("@info:tooltip %1 is an app name", "%1\nMiddle-click to pause\nScroll to adjust volume", root.identity)
                case Mpris.PlaybackStatus.Paused:
                    return root.artist ? i18nc("@info:tooltip %1 is a musical artist and %2 is an app name", "by %1 (paused, %2)\nMiddle-click to play\nScroll to adjust volume", root.artist, root.identity)
                    : i18nc("@info:tooltip %1 is an app name", "Paused (%1)\nMiddle-click to play\nScroll to adjust volume", root.identity)
                default:
                    return "";
            }
            toolTipTextFormat: Text.PlainText

            compactRepresentation: CompactRepresentation {}
            fullRepresentation: ExpandedRepresentation {}

            // HACK Some players like Amarok take quite a while to load the next track
            // this avoids having the plasmoid jump between popup and panel
            onPlaybackStatusChanged: {
                if (root.playbackStatus > Mpris.PlaybackStatus.Stopped) {
                    Plasmoid.status = PlasmaCore.Types.ActiveStatus
                } else {
                    updatePlasmoidStatusTimer.restart()
                }
            }

            onExpandedChanged: {
                if (root.expanded) {
                    mpris2Model.currentPlayer?.updatePosition();
                }
            }

            Timer {
                id: updatePlasmoidStatusTimer
                interval: Kirigami.Units.humanMoment
                onTriggered: {
                    if (root.playbackStatus > Mpris.PlaybackStatus.Stopped) {
                        Plasmoid.status = PlasmaCore.Types.ActiveStatus
                    } else {
                        Plasmoid.status = PlasmaCore.Types.PassiveStatus
                    }
                }
            }

            Plasmoid.contextualActions: [
                PlasmaCore.Action {
                    text: i18nc("Open player window or bring it to the front if already open", "Open")
                    icon.name: "go-up-symbolic"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canRaise
                    onTriggered: root.raise()
                },
                PlasmaCore.Action {
                    text: i18nc("Play previous track", "Previous Track")
                    icon.name: Application.layoutDirection === Qt.RightToLeft ? "media-skip-forward" : "media-skip-backward"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canControl
                    enabled: root.canGoPrevious
                    onTriggered: root.previous()
                },
                PlasmaCore.Action {
                    text: i18nc("Pause playback", "Pause")
                    icon.name: "media-playback-pause"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.isPlaying && root.canPause
                    enabled: visible
                    onTriggered: root.pause()
                },
                PlasmaCore.Action {
                    text: i18nc("Start playback", "Play")
                    icon.name: "media-playback-start"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canControl && !root.isPlaying
                    enabled: root.canPlay
                    onTriggered: root.play()
                },
                PlasmaCore.Action {
                    text: i18nc("Play next track", "Next Track")
                    icon.name: Application.layoutDirection === Qt.RightToLeft ? "media-skip-backward" : "media-skip-forward"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canControl
                    enabled: root.canGoNext
                    onTriggered: root.next()
                },
                PlasmaCore.Action {
                    text: i18nc("Stop playback", "Stop")
                    icon.name: "media-playback-stop"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canControl
                    enabled: root.canStop
                    onTriggered: root.stop()
                },
                PlasmaCore.Action {
                    isSeparator: true
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canQuit
                },
                PlasmaCore.Action {
                    text: i18nc("Quit player", "Quit")
                    icon.name: "application-exit"
                    priority: PlasmaCore.Action.LowPriority
                    visible: root.canQuit
                    onTriggered: root.quit()
                }
            ]
            function previous(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Previous();
                }
            }
            function next(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Next();
                }
            }
            function play(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Play();
                }
            }
            function pause(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Pause();
                }
            }
            function togglePlaying(): void {
                if (mpris2Model.currentPlayer) {
                    if (root.isPlaying) {
                        mpris2Model.currentPlayer.Pause();
                    } else {
                        mpris2Model.currentPlayer.Play();
                    }
                }
            }
            function stop(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Stop();
                }
            }
            function quit(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Quit();
                }
            }
            function raise(): void {
                if (mpris2Model.currentPlayer) {
                    mpris2Model.currentPlayer.Raise();
                }
            }
            Mpris.Mpris2Model {
                id: mpris2Model
            }
            Component.onCompleted: {
                Plasmoid.removeInternalAction("configure");
                refreshExtraMetadata();
            }
}
