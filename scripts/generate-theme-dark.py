from colormath.color_objects import LCHabColor, sRGBColor
from colormath.color_conversions import convert_color

from sys import argv
import json


def main():
    if (len(argv) == 10):
        name = str(argv[1])
        
        fg = int(argv[2])
        bg = int(argv[3])
        red = int(argv[4])
        yellow = int(argv[5])
        green = int(argv[6])
        cyan = int(argv[7])
        blue = int(argv[8])
        magenta = int(argv[9])

        generateUniColorVsCodeTheme(name, fg, bg, red, green, yellow, blue, magenta, cyan)
    else:
        print('Expecting color theme name and 8 LCH hue values.')


def generateUniColorVsCodeTheme(name, fg, bg, red, green, yellow, blue, magenta, cyan):
    '''
    Generates VS Code color theme JSON file from given hues and name.
    Filename is generated automatically based on given name.
    '''
    colors = _generateThemeHexValues(fg, bg, red, green, yellow, blue, magenta, cyan)
    filename = name.lower().replace(' ', '-').replace('&', 'and') + '-color-theme.json'
    with open(filename, 'w') as f:
        json.dump(_generateJsonContent(name, colors), f, indent='\t')
    print('Generated color theme:', filename)


def _generateThemeHexValues(fg, bg, red, green, yellow, blue, magenta, cyan):
    '''
    Takes LCH hue values from 0-360 and generates list of RGB hex values for color theme.
    '''
    obs = '2'
    ill = 'd50'
    fgChroma = 5
    lch_colors = {
        # Neutral foreground
        'fg45':     LCHabColor(45, fgChroma, fg, obs, ill), # whitespace foreground
        'fg60':     LCHabColor(60, fgChroma, fg, obs, ill),
        'fg75':     LCHabColor(75, fgChroma, fg, obs, ill), # main foreground, entities, cursor, markup italic
        'fg90':     LCHabColor(90, fgChroma, fg, obs, ill), # method/function declarations, markup bold

        # Background
        'bg00':     LCHabColor(0, 0, 0, obs, ill),
        'bg05':     LCHabColor(5, 0, bg, obs, ill), # main background
        'bg10':     LCHabColor(10, 0, bg, obs, ill), # line highlight
        'bg15':     LCHabColor(15, 0, bg, obs, ill),
        'bg20':     LCHabColor(20, 0, bg, obs, ill), # selection
        'bg25':     LCHabColor(25, 0, bg, obs, ill), # hover highlight
        'bg35':     LCHabColor(35, 0, bg, obs, ill),

        # Main non-neutral foreground
        'red':                  LCHabColor(60, 60, red, obs, ill), # errors, invalid, diff delete
        'green':                LCHabColor(60, 50, green, obs, ill), # strings, CSS tags, markup code, diff insert
        'yellow':               LCHabColor(60, 55, yellow, obs, ill), # variables, HTML tags, markup heading
        'blue':                 LCHabColor(60, 50, blue, obs, ill), # storage types, attributes, markup underline, diff change
        'magenta':              LCHabColor(60, 60, magenta, obs, ill), # keywords, storage, tags
        'cyan':                 LCHabColor(60, 35, cyan, obs, ill), # comments, markup quote
        'lightPink':            LCHabColor(75, 40, red-30, obs, ill),
        'lightGreen':           LCHabColor(80, 50, green-30, obs, ill),
        'lightOrange':          LCHabColor(80, 40, yellow-30, obs, ill),
        'lightBlue':            LCHabColor(80, 35, blue-30, obs, ill),
        'lightPurple':          LCHabColor(80, 34, magenta-30, obs, ill), # constants
        'lightTurquoise':       LCHabColor(80, 50, cyan-30, obs, ill),

        # Other
        'black':        LCHabColor(20, 0, 0, obs, ill),
        'brightBlack':  LCHabColor(60, 0, 0, obs, ill),
        'white':        LCHabColor(80, 0, 0, obs, ill),
        'brightWhite':  LCHabColor(100, 0, 0, obs, ill),
        'orange':       LCHabColor(60, 60, yellow-30, obs, ill), # warnings
        'darkRed':      LCHabColor(20, 20, red, obs, ill),
        'darkOrange':   LCHabColor(20, 20, yellow-30, obs, ill),
        'darkBlue':     LCHabColor(20, 20, blue, obs, ill),
        'dullRed':      LCHabColor(60, 30, red, obs, ill),
        'dullOrange':   LCHabColor(60, 30, yellow-30, obs, ill),
        'dullGreen':    LCHabColor(60, 25, green, obs, ill),
        'dullBlue':     LCHabColor(60, 25, blue, obs, ill),

        # Only for UI
        'focusBorder':      LCHabColor(40, 40, magenta-30, obs, ill),
        'btnBadgeBg':       LCHabColor(40, 25, magenta-30, obs, ill),
        'btnBadgeHoverBg':  LCHabColor(47, 25, magenta-30, obs, ill),
        'findMatchBg':      LCHabColor(35, 25, cyan-30, obs, ill),
        'findMatchHlBg':    LCHabColor(25, 20, yellow-30, obs, ill),
        'listActiveSelBg':  LCHabColor(25, 20, magenta-30, obs, ill),
        'progressBarBg':    LCHabColor(45, 50, blue-30, obs, ill),
        'border':           LCHabColor(20, fgChroma, fg, obs, ill),
        'checkboxBorder':   LCHabColor(40, fgChroma, fg, obs, ill),
    }

    rgb_colors = {}
    for key, value in lch_colors.items():
        rgb_r, rgb_g, rgb_b = convert_color(
            value, sRGBColor).get_upscaled_value_tuple()
        rgb_colors[key] = "#%02x%02x%02x" % (
            _clamp(rgb_r), _clamp(rgb_g), _clamp(rgb_b))

    return rgb_colors


def _clamp(x):
    return max(0, min(x, 255))


def _generateJsonContent(name, colors):
    '''
    Generates the JSON file for the color theme.
    Colors is the dict of hex values.
    '''
    return {
        'name': name,
        'colors': {
            'editor.background': colors['bg05'],
            'editor.foreground': colors['fg75'],
            'editor.lineHighlightBackground': colors['bg10'],
            'editor.selectionBackground': colors['bg20'],
            'editorCursor.foreground': colors['fg75'],
            'editorWhitespace.foreground': colors['fg45'],

            # base colors (used as defaults unless overwritten by more specific rule)
            'descriptionForeground': colors['fg75'] + 'b3',
            'errorForeground': colors['red'],
            'focusBorder': colors['focusBorder'] + 'cc',
            'foreground': colors['fg75'],
            'icon.foreground': colors['fg75'],
            'selection.background': colors['bg35'] + '80',

            # UI
            'activityBar.background': colors['bg20'],
            'activityBar.foreground': colors['fg90'],
            'activityBarBadge.background': colors['btnBadgeBg'],
            'activityBarBadge.foreground': colors['fg90'],
            'badge.background': colors['bg25'],
            'badge.foreground': colors['fg90'],
            'button.background': colors['btnBadgeBg'],
            'button.foreground': colors['fg90'],
            'button.hoverBackground': colors['btnBadgeHoverBg'],
            'debugToolBar.background': colors['bg15'],
            'diffEditor.insertedTextBackground': colors['green'] + '33',
            'diffEditor.removedTextBackground': '#ff000033',
            'dropdown.background': colors['bg10'],
            'dropdown.foreground': colors['fg90'],
            'editor.findMatchBackground': colors['findMatchBg'],
            'editor.findMatchBorder': colors['orange'],
            'editor.findMatchHighlightBackground': colors['findMatchHlBg'],
            'editor.findRangeHighlightBackground': colors['bg20'] + '66',
            'editor.hoverHighlightBackground': colors['bg25'] + '40',
            'editor.inactiveSelectionBackground': colors['bg20'] + 'a4',
            'editor.lineHighlightBorder': colors['bg10'],
            'editor.linkedEditingBackground': colors['blue'] + '4d',
            'editor.selectionHighlightBackground': colors['yellow'] + '18',
            'editor.wordHighlightBackground': colors['green'] + '30',
            'editor.wordHighlightStrongBackground': colors['orange'] + '30',
            'editorBracketHighlight.foreground1': colors['fg75'],
            'editorBracketHighlight.foreground2': colors['yellow'],
            'editorBracketHighlight.foreground3': colors['green'],
            'editorBracketHighlight.foreground4': colors['cyan'],
            'editorBracketHighlight.foreground5': colors['blue'],
            'editorBracketHighlight.foreground6': colors['magenta'],
            'editorBracketHighlight.unexpectedBracket.foreground': colors['red'],
            'editorBracketMatch.background': colors['bg35'] + '1a',
            'editorBracketMatch.border': colors['fg60'],
            'editorCodeLens.foreground': colors['fg75'],
            'editorError.foreground': colors['red'],
            'editorGroup.border': colors['fg45'],
            'editorGroup.dropBackground': colors['bg25'] + '80',
            'editorGroup.emptyBackground': colors['bg05'],
            'editorGroupHeader.noTabsBackground': colors['bg05'],
            'editorGroupHeader.tabsBackground': colors['bg10'],
            'editorGutter.addedBackground': colors['green'],
            'editorGutter.background': colors['bg05'],
            'editorGutter.deletedBackground': colors['red'],
            'editorGutter.modifiedBackground': colors['blue'],
            'editorHoverWidget.background': colors['bg10'],
            'editorHoverWidget.border': colors['border'],
            'editorIndentGuide.activeBackground': colors['bg35'],
            'editorIndentGuide.background': colors['bg20'],
            'editorInfo.foreground': colors['blue'],
            'editorLineNumber.activeForeground': colors['fg75'],
            'editorLineNumber.foreground': colors['fg45'],
            'editorOverviewRuler.addedForeground': colors['green'] + '99',
            'editorOverviewRuler.border': colors['fg60'] + '4d',
            'editorOverviewRuler.commonContentForeground': colors['fg60'] + '66',
            'editorOverviewRuler.currentContentForeground': colors['fg75'] + '80',
            'editorOverviewRuler.deletedForeground': colors['red'] + '99',
            'editorOverviewRuler.errorForeground': colors['red'] + 'b3',
            'editorOverviewRuler.findMatchForeground': colors['orange'] + '7e',
            'editorOverviewRuler.incomingContentForeground': colors['blue'] + '80',
            'editorOverviewRuler.infoForeground': colors['blue'],
            'editorOverviewRuler.modifiedForeground': colors['blue'] + '99',
            'editorOverviewRuler.rangeHighlightForeground': colors['blue'] + '99',
            'editorOverviewRuler.selectionHighlightForeground': colors['fg60'] + 'cc',
            'editorOverviewRuler.warningForeground': colors['orange'],
            'editorOverviewRuler.wordHighlightForeground': colors['fg60'] + 'cc',
            'editorOverviewRuler.wordHighlightStrongForeground': colors['fg75'] + 'cc',
            'editorRuler.foreground': colors['fg45'],
            'editorSuggestWidget.background': colors['bg10'],
            'editorSuggestWidget.border': colors['border'],
            'editorSuggestWidget.foreground': colors['fg90'],
            'editorSuggestWidget.highlightForeground': colors['green'],
            'editorSuggestWidget.selectedBackground': colors['bg15'],
            'editorUnnecessaryCode.opacity': colors['bg00'] + 'c0',
            'editorWarning.foreground': colors['orange'],
            'editorWidget.background': colors['bg10'],
            'editorWidget.border': colors['bg25'],
            'gitDecoration.conflictingResourceForeground': colors['red'],
            'gitDecoration.deletedResourceForeground': colors['dullRed'],
            'gitDecoration.stageDeletedResourceForeground': colors['dullRed'],
            'gitDecoration.ignoredResourceForeground': colors['fg60'],
            'gitDecoration.modifiedResourceForeground': colors['dullBlue'],
            'gitDecoration.stageModifiedResourceForeground': colors['dullBlue'],
            'gitDecoration.untrackedResourceForeground': colors['dullGreen'],
            'gitDecoration.addedResourceForeground': colors['dullGreen'],
            'gitDecoration.renamedResourceForeground': colors['dullGreen'],
            'gitDecoration.submoduleResourceForeground': colors['dullOrange'],
            'input.background': colors['bg00'],
            'input.border': colors['border'],
            'input.foreground': colors['fg75'],
            'input.placeholderForeground': colors['fg60'],
            'inputOption.activeBorder': colors['green'],
            'inputValidation.errorBackground': colors['darkRed'],
            'inputValidation.errorBorder': colors['red'],
            'inputValidation.infoBackground': colors['darkBlue'],
            'inputValidation.infoBorder': colors['blue'],
            'inputValidation.warningBackground': colors['darkOrange'],
            'inputValidation.warningBorder': colors['orange'],
            'list.activeSelectionBackground': colors['listActiveSelBg'],
            'list.activeSelectionForeground': colors['fg90'],
            'list.dropBackground': colors['bg20'],
            'list.focusBackground': colors['bg20'],
            'list.highlightForeground': colors['fg90'],
            'list.hoverBackground': colors['bg15'],
            'list.inactiveSelectionBackground': colors['bg15'],
            'list.inactiveSelectionForeground': colors['fg90'],
            'merge.currentContentBackground': colors['green'] + '33',
            'merge.currentHeaderBackground': colors['green'] + '80',
            'merge.incomingContentBackground': colors['blue'] + '33',
            'merge.incomingHeaderBackground': colors['blue'] + '80',
            'notifications.background': colors['bg10'],
            'panel.border': colors['fg60'] + '59',
            'panelTitle.activeForeground': colors['fg90'],
            'peekView.border': colors['lightGreen'],
            'peekViewEditor.background': colors['bg10'] + '66',
            'peekViewEditor.matchHighlightBackground': colors['findMatchHlBg'],
            'peekViewEditorGutter.background': colors['bg10'] + '66',
            'peekViewResult.background': colors['bg10'],
            'peekViewResult.fileForeground': colors['fg90'],
            'peekViewResult.matchHighlightBackground': colors['findMatchHlBg'],
            'peekViewResult.selectionBackground': colors['green'] + '33',
            'peekViewResult.selectionForeground': colors['fg90'],
            'peekViewTitle.background': colors['bg10'] + '66',
            'peekViewTitleDescription.foreground': colors['fg75'] + 'b3',
            'peekViewTitleLabel.foreground': colors['fg90'],
            'progressBar.background': colors['progressBarBg'],
            'scrollbar.shadow': colors['bg00'],
            'scrollbarSlider.activeBackground': colors['fg60'] + '80',
            'scrollbarSlider.background': colors['bg25'] + '80',
            'scrollbarSlider.hoverBackground': colors['bg35'] + '80',
            'settings.checkboxBackground': colors['bg00'],
            'settings.checkboxBorder': colors['checkboxBorder'],
            'settings.dropdownBackground': colors['bg00'],
            'settings.dropdownBorder': colors['border'],
            'settings.dropdownListBorder': colors['border'],
            'settings.numberInputBackground': colors['bg00'],
            'settings.numberInputBorder': colors['border'],
            'settings.textInputBackground': colors['bg00'],
            'settings.textInputBorder': colors['border'],
            'sideBar.background': colors['bg10'],
            'sideBarSectionHeader.background': colors['bg15'],
            'sideBarTitle.foreground': colors['fg75'],
            'statusBar.background': colors['bg20'],
            'statusBar.debuggingBackground': colors['bg20'],
            'statusBar.debuggingForeground': colors['fg90'],
            'statusBar.foreground': colors['fg75'],
            'statusBar.noFolderBackground': colors['bg20'],
            'tab.activeBackground': colors['bg05'],
            'tab.activeForeground': colors['fg90'],
            'tab.border': colors['bg05'],
            'tab.inactiveBackground': colors['bg15'],
            'tab.inactiveForeground': colors['fg90'] + '80',
            'tab.unfocusedActiveForeground': colors['fg90'] + '80',
            'tab.unfocusedInactiveForeground': colors['fg90'] + '40',
            'textLink.activeForeground': colors['blue'],
            'textLink.foreground': colors['blue'],
            'titleBar.activeBackground': colors['bg25'],
            'titleBar.activeForeground': colors['fg90'],
            'titleBar.inactiveBackground': colors['bg25'],
            'titleBar.inactiveForeground': colors['fg75'],
            'widget.shadow': colors['bg00'] + '5c',

            # TERMINAL
            'terminal.foreground':          colors['fg75'],
            'terminal.background':          colors['bg05'],
            'terminal.ansiBlack':           colors['black'],
            'terminal.ansiBrightBlack':     colors['brightBlack'],
            'terminal.ansiBlue':            colors['blue'],
            'terminal.ansiBrightBlue':      colors['lightBlue'],
            'terminal.ansiCyan':            colors['cyan'],
            'terminal.ansiBrightCyan':      colors['lightTurquoise'],
            'terminal.ansiGreen':           colors['green'],
            'terminal.ansiBrightGreen':     colors['lightGreen'],
            'terminal.ansiMagenta':         colors['magenta'],
            'terminal.ansiBrightMagenta':   colors['lightPurple'],
            'terminal.ansiRed':             colors['red'],
            'terminal.ansiBrightRed':       colors['lightPink'],
            'terminal.ansiYellow':          colors['yellow'],
            'terminal.ansiBrightYellow':    colors['lightOrange'],
            'terminal.ansiWhite':           colors['white'],
            'terminal.ansiBrightWhite':     colors['brightWhite'],
        },
        'tokenColors': [
            {
                'name': 'Keyword, storage, tag',
                'scope': [
                    'keyword',
                    'storage',
                    'entity.name.tag',
                ],
                'settings': {
                    'foreground': colors['magenta']
                }
            },
            {
                'name': 'HTML tag',
                'scope': [
                    'entity.name.tag.html'
                ],
                'settings': {
                    'foreground': colors['yellow']
                }
            },
            {
                'name': 'CSS Tag',
                'scope': [
                    'entity.name.tag.css'
                ],
                'settings': {
                    'foreground': colors['green']
                }
            },
            {
                'name': 'Storage type, attribute',
                'scope': [
                    'storage.type',
                    'entity.other.attribute-name'
                ],
                'settings': {
                    'foreground': colors['blue'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Entity',
                'scope': [
                    'entity.name',
                    'entity.other.inherited-class',
                ],
                'settings': {
                    'foreground': colors['fg75']
                }
            },
            {
                'name': 'Library entity',
                'scope': 'support',
                'settings': {
                    'foreground': colors['fg75'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Variable',
                'scope': [
                    'variable',
                    'variable.language',
                    'variable.parameter'
                ],
                'settings': {
                    'foreground': colors['yellow']
                }
            },
            {
                'name': 'Library variable',
                'scope': [
                    'support.variable',
                    'support.other.variable'
                ],
                'settings': {
                    'foreground': colors['yellow']
                }
            },
            {
                'name': 'Constant',
                'scope': [
                    'constant',
                    'constant.numeric',
                    'constant.language',
                    'constant.character.escape',
                    'constant.other',
                    'keyword.other.unit.px.css'
                ],
                'settings': {
                    'foreground': colors['lightPurple']
                }
            },
            {
                'name': 'Library constant',
                'scope': 'support.constant',
                'settings': {
                    'foreground': colors['lightPurple'],
                    'fontStyle': ''
                }
            },
            {
                'name': 'String',
                'scope': 'string',
                'settings': {
                    'foreground': colors['green']
                }
            },
            {
                'name': 'Comment',
                'scope': 'comment',
                'settings': {
                    'foreground': colors['cyan'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Diff delete',
                'scope': 'markup.deleted',
                'settings': {
                    'foreground': colors['red']
                }
            },
            {
                'name': 'Diff insert',
                'scope': 'markup.inserted',
                'settings': {
                    'foreground': colors['green']
                }
            },
            {
                'name': 'Diff change',
                'scope': 'markup.changed',
                'settings': {
                    'foreground': colors['blue']
                }
            },
            {
                'name': 'Markup heading',
                'scope': [
                    'markup.heading',
                    'entity.name.section'
                ],
                'settings': {
                    'foreground': colors['yellow']
                }
            },
            {
                'name': 'Markup bold',
                'scope': [
                    'markup.bold'
                ],
                'settings': {
                    'foreground': colors['fg90'],
                    'fontStyle': 'bold'
                }
            },
            {
                'name': 'Markup italic',
                'scope': [
                    'markup.italic'
                ],
                'settings': {
                    'foreground': colors['fg75'],
                    'fontStyle': 'italic'
                }
            },
            {
                'name': 'Markup underline',
                'scope': [
                    'markup.underline'
                ],
                'settings': {
                    'foreground': colors['blue'],
                    'fontStyle': 'underline'
                }
            },
            {
                'name': 'Markup code',
                'scope': [
                    'markup.inline.raw',
                    'markup.fenced_code',
                    'markup.raw'
                ],
                'settings': {
                    'foreground': colors['green']
                }
            },
            {
                'name': 'Markup quote',
                'scope': [
                    'markup.quote'
                ],
                'settings': {
                    'foreground': colors['cyan']
                }
            },
            {
                'name': 'Invalid',
                'scope': 'invalid',
                'settings': {
                    'foreground': colors['red']
                }
            }
        ],
        'semanticHighlighting': 'true',
        'semanticTokenColors': {
            'method.declaration': {
                'foreground': colors['fg90'],
                'bold': 'true'
            },
            'function.declaration': {
                'foreground': colors['fg90'],
                'bold': 'true'
            }
        }
    }


if __name__ == '__main__':
    main()
