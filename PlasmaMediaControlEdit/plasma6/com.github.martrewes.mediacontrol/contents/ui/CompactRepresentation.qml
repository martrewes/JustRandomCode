/*
 *    SPDX-FileCopyrightText: 2022 Fushan Wen <qydwhotmail@gmail.com>
 *
 *    SPDX-License-Identifier: GPL-2.0-or-later
 */
pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Layouts

import org.kde.plasma.core as PlasmaCore
import org.kde.plasma.components as PC3
import org.kde.plasma.plasmoid
import org.kde.kirigami as Kirigami

/**
 * [Album Art][Now Playing]
 */
Loader {
    id: compactRepresentation

    // Adjust this multiplier (e.g., 16 to 20) to fine-tune the exact max text width
    readonly property real maxTextWidth: Kirigami.Units.gridUnit * 10

    Layout.fillWidth: layoutForm !== CompactRepresentation.LayoutType.HorizontalPanel && layoutForm !== CompactRepresentation.LayoutType.HorizontalDesktop
    Layout.fillHeight: layoutForm !== CompactRepresentation.LayoutType.VerticalPanel && layoutForm !== CompactRepresentation.LayoutType.VerticalDesktop

    Layout.preferredWidth: {
        switch (compactRepresentation.layoutForm) {
            case CompactRepresentation.LayoutType.HorizontalPanel:
                return implicitWidth + (root.track == "" ? 0 : Kirigami.Units.smallSpacing * 2);
            default:
                return -1;
        }
    }
    Layout.preferredHeight: {
        switch (compactRepresentation.layoutForm) {
            case CompactRepresentation.LayoutType.VerticalPanel:
            case CompactRepresentation.LayoutType.VerticalDesktop:
                return implicitHeight;
            default:
                return -1;
        }
    }

    Layout.maximumWidth: layoutForm === CompactRepresentation.LayoutType.HorizontalPanel
    ? (maxTextWidth + compactRepresentation.height + Kirigami.Units.smallSpacing * 3)
    : -1

    enum LayoutType {
        Tray,
        HorizontalPanel,
        VerticalPanel,
        HorizontalDesktop,
        VerticalDesktop,
        IconOnly
    }

    readonly property int layoutForm: {
        if (compactRepresentation.inTray) {
            return CompactRepresentation.LayoutType.Tray;
        } else if (compactRepresentation.inPanel) {
            return compactRepresentation.isVertical ? CompactRepresentation.LayoutType.VerticalPanel : CompactRepresentation.LayoutType.HorizontalPanel;
        } else if (compactRepresentation.item instanceof GridLayout) {
            if (compactRepresentation.parent.width > compactRepresentation.parent.height + (compactRepresentation.item as GridLayout).columnSpacing) {
                return CompactRepresentation.LayoutType.HorizontalDesktop;
            } else if (compactRepresentation.parent.height - compactRepresentation.parent.width >= compactRepresentation.item.labelHeight + (compactRepresentation.item as GridLayout).rowSpacing) {
                return CompactRepresentation.LayoutType.VerticalDesktop;
            }
        }
        return CompactRepresentation.LayoutType.IconOnly;
    }
    readonly property bool isVertical: Plasmoid.formFactor === PlasmaCore.Types.Vertical
    readonly property bool inPanel: [PlasmaCore.Types.TopEdge, PlasmaCore.Types.RightEdge, PlasmaCore.Types.BottomEdge, PlasmaCore.Types.LeftEdge].includes(Plasmoid.location)
    readonly property bool inTray: parent.objectName === "org.kde.desktop-CompactApplet"

    sourceComponent: inTray || root.track.length === 0 ? icon : playerRow

    MouseArea {
        id: mouseArea
        anchors.fill: parent
        acceptedButtons: Qt.LeftButton | Qt.MiddleButton | Qt.BackButton | Qt.ForwardButton
        hoverEnabled: compactRepresentation.item instanceof Kirigami.Icon
        property int wheelDelta: 0
        onWheel: wheel => {
            if (mpris2Model.currentPlayer === null) {
                return;
            }
            wheelDelta += (wheel.inverted ? -1 : 1) * (wheel.angleDelta.y ? wheel.angleDelta.y : -wheel.angleDelta.x)
            while (wheelDelta >= 120) {
                wheelDelta -= 120;
                mpris2Model.currentPlayer.changeVolume(root.volumePercentStep / 100, true);
            }
            while (wheelDelta <= -120) {
                wheelDelta += 120;
                mpris2Model.currentPlayer.changeVolume(-root.volumePercentStep / 100, true);
            }
        }
        onClicked: (mouse) => {
            switch (mouse.button) {
                case Qt.MiddleButton:
                    root.togglePlaying()
                    break
                case Qt.BackButton:
                    if (root.canGoPrevious) {
                        root.previous();
                    }
                    break
                case Qt.ForwardButton:
                    if (root.canGoNext) {
                        root.next();
                    }
                    break
                default:
                    root.expanded = !root.expanded
            }
        }
    }

    Component {
        id: icon
        Kirigami.Icon {
            active: mouseArea.containsMouse
            source: Plasmoid.icon
        }
    }

    Component {
        id: playerRow
        GridLayout {
            id: grid
            readonly property real labelHeight: songTitle.implicitHeight

            rowSpacing: Kirigami.Units.smallSpacing
            columnSpacing: rowSpacing
            flow: {
                switch (compactRepresentation.layoutForm) {
                    case CompactRepresentation.LayoutType.VerticalPanel:
                    case CompactRepresentation.LayoutType.VerticalDesktop:
                        return GridLayout.TopToBottom;
                    default:
                        return GridLayout.LeftToRight;
                }
            }

            Item {
                id: spacerItem
                visible: compactRepresentation.layoutForm === CompactRepresentation.LayoutType.VerticalDesktop
                Layout.fillHeight: true
            }

            AlbumArtStackView {
                id: albumArt

                Layout.alignment: Qt.AlignVCenter
                Layout.fillWidth: compactRepresentation.Layout.fillWidth
                Layout.fillHeight: compactRepresentation.Layout.fillHeight
                Layout.preferredWidth: compactRepresentation.Layout.fillWidth ? -1 : compactRepresentation.height
                Layout.preferredHeight: compactRepresentation.Layout.fillHeight ? -1 : compactRepresentation.width

                inCompactRepresentation: true

                Connections {
                    target: root

                    function onAlbumArtChanged() {
                        albumArt.loadAlbumArt();
                    }
                }

                Component.onCompleted: albumArt.loadAlbumArt()
            }

            ColumnLayout {
                id: textColumn
                Layout.alignment: Qt.AlignVCenter
                Layout.maximumWidth: compactRepresentation.layoutForm === CompactRepresentation.LayoutType.HorizontalPanel
                ? compactRepresentation.maxTextWidth
                : -1
                visible: compactRepresentation.layoutForm !== CompactRepresentation.LayoutType.VerticalPanel && compactRepresentation.layoutForm !== CompactRepresentation.LayoutType.IconOnly
                || (compactRepresentation.layoutForm === CompactRepresentation.LayoutType.VerticalPanel && compactRepresentation.parent.width >= Kirigami.Units.gridUnit * 5)

                spacing: 0

                // Shared synchronization state for both lines
                property real scrollProgress: 0.0
                readonly property real maxOverflow: Math.max(titleClip.overflow, artistClip.visible ? artistClip.overflow : 0)
                readonly property bool shouldScroll: maxOverflow > 0

                function resetMarquee(): void {
                    syncMarquee.stop();
                    scrollProgress = 0.0;
                    if (shouldScroll && visible) {
                        syncMarquee.start();
                    }
                }

                SequentialAnimation on scrollProgress {
                    id: syncMarquee
                    running: textColumn.shouldScroll && textColumn.visible
                    loops: Animation.Infinite

                    PauseAnimation { duration: 2000 }
                    NumberAnimation {
                        from: 0.0
                        to: 1.0
                        duration: Math.max(1000, textColumn.maxOverflow * 30)
                        easing.type: Easing.Linear
                    }
                    PauseAnimation { duration: 2000 }
                    NumberAnimation {
                        from: 1.0
                        to: 0.0
                        duration: Math.max(1000, textColumn.maxOverflow * 25)
                        easing.type: Easing.InOutQuad
                    }
                }

                // Song Title (Line 1)
                Item {
                    id: titleClip
                    Layout.fillWidth: true
                    implicitWidth: songTitle.implicitWidth
                    implicitHeight: songTitle.implicitHeight
                    clip: true

                    readonly property real overflow: Math.max(0, songTitle.implicitWidth - titleClip.width)

                    PC3.Label {
                        id: songTitle
                        height: titleClip.height
                        verticalAlignment: Text.AlignVCenter
                        textFormat: Text.PlainText
                        wrapMode: Text.NoWrap

                        opacity: root.isPlaying ? 1 : 0.75
                        Behavior on opacity {
                            NumberAnimation {
                                duration: Kirigami.Units.longDuration
                                easing.type: Easing.InOutQuad
                            }
                        }

                        x: (!textColumn.shouldScroll && grid.flow === GridLayout.TopToBottom)
                        ? Math.max(0, (titleClip.width - songTitle.implicitWidth) / 2)
                        : (-titleClip.overflow * textColumn.scrollProgress)

                        text: root.trackNo + root.track + root.trackLength
                        onTextChanged: textColumn.resetMarquee()
                    }
                }
                // Song Artist / Album / Year (Line 2)
                Item {
                    id: artistClip
                    Layout.fillWidth: true
                    implicitWidth: songArtist.implicitWidth
                    implicitHeight: songArtist.implicitHeight
                    clip: true
                    visible: root.artist.length > 0 && compactRepresentation.height >= songTitle.implicitHeight + songArtist.implicitHeight * 0.8 /* For CJK */ + (compactRepresentation.layoutForm === CompactRepresentation.LayoutType.VerticalDesktop ? albumArt.height + grid.rowSpacing : 0)
                    readonly property real overflow: Math.max(0, songArtist.implicitWidth - artistClip.width)
                    PC3.Label {
                        id: songArtist
                        height: artistClip.height
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: Kirigami.Theme.smallFont.pointSize
                        opacity: 0.75
                        textFormat: Text.PlainText
                        wrapMode: Text.NoWrap
                        x: (!textColumn.shouldScroll && grid.flow === GridLayout.TopToBottom)
                        ? Math.max(0, (artistClip.width - songArtist.implicitWidth) / 2)
                        : (-artistClip.overflow * textColumn.scrollProgress)
                        text: root.artist + root.customAlbum + root.trackDate
                        onTextChanged: textColumn.resetMarquee()
                    }
                }
            }
            Item {
                visible: spacerItem.visible
                Layout.fillHeight: true
            }
        }
    }
}
