# Stained Glass Theme for VS Code

A theme designed with LCH color values to get more perceptually uniform hues and contrast.

## Palette

- Italics are used for comments, library/support entities, storage types, attributes, and markup italic.
- Bold is used for method/function declarations and markup bold.
- For LCH values:
    - CIE standard observer = 2
    - CIE standard illuminant = D50

### Background

color               | LCH value     | RGB hex value | notes
---                 | ---           | ---           | ---
black               | 0, 0, 0       | `#000000`       |
bg5                 | 5, 0, 0       | `#111111`       | main background
bg10                | 10, 0, 0      | `#1b1b1b`       | line highlight
bg15                | 15, 0, 0      | `#262626`       |
bg20                | 20, 0, 0      | `#303030`       | selection
bg25                | 25, 0, 0      | `#3b3b3b`       | hover highlight
bg35                | 35, 0, 0      | `#525252`       |

### Neutral foreground

color               | LCH value     | RGB hex value | notes
---                 | ---           | ---           | ---
fg45                | 45, 5, 60     | `#716963`       | whitespace foreground
fg60                | 60, 5, 60     | `#988f89`       |
fg75                | 75, 5, 60     | `#c0b7b1`       | main foreground, entities, cursor, markup italic
fg90                | 90, 5, 60     | `#eae1da`       | method/function declarations, markup bold

### Main non-neutral foreground

color           | LCH value     | RGB hex value | notes
---             | ---           | ---           | ---
red             | 60, 60, 30    | `#e9655f`       | terminal red, errors, invalid, diff delete
green           | 60, 50, 150   | `#39a462`       | terminal green, strings, CSS tags, markup code, diff insert
yellow          | 60, 55, 90    | `#a48f25`       | terminal yellow, variables, HTML tags, markup heading
blue            | 60, 50, 270   | `#5793e9`       | terminal blue, storage types, attributes, markup underline, diff change
magenta         | 60, 60, 330   | `#d469c7`       | terminal magenta, keywords, storage, tags
cyan            | 60, 35, 210   | `#20a0ae`       | terminal cyan, comments, markup quote
lightPink       | 80, 0, 0      | `#fc9bbb`       | terminal brightRed
lightGreen      | 75, 40, 0     | `#acd372`       | terminal brightGreen
lightOrange     | 80, 50, 120   | `#f9b887`       | terminal brightYellow
lightBlue       | 80, 40, 60    | `#7ed2fe`       | terminal brightBlue
lightPurple     | 80, 35, 240   | `#d2bdfe`       | terminal brightMagenta, constants
lightTurquoise  | 80, 34, 300   | `#24dfc4`       | terminal brightCyan

### Only used for terminal

color       | LCH value     | RGB hex value | notes
---         | ---           | ---           | ---
black       | 20, 0, 0      | `#303030`       | terminal black
brightBlack | 60, 0, 0      | `#919191`       | terminal brightBlack
white       | 80, 50, 180   | `#c6c6c6`       | terminal white
brightWhite | 100, 0, 0     | `#ffffff`       | terminal brightWhite

### Errors, warnings, info, git

color       | LCH value     | RGB hex value | notes
---         | ---           | ---           | ---
orange      | 60, 60, 60    | `#cf7a33`       | warnings
darkRed     | 20, 20, 30    | `#4a2623`       |
darkOrange  | 20, 20, 60    | `#432a17`       |
darkBlue    | 20, 20, 270   | `#1f314e`       |
dullRed     | 60, 30, 30    | `#c17f78`       |
dullOrange  | 60, 30, 60    | `#b48663`       |
dullGreen   | 60, 25, 150   | `#6d9b7a`       |
dullBlue    | 60, 25, 270   | `#7c92bc`       |

### Misc

color               | LCH value     | RGB hex value | notes
---                 | ---           | ---           | ---
focusBorder         | 40, 40, 300   | `#675497`       |
btnBadgeBg          | 40, 25, 300   | `#655882`       |
btnBadgeHoverBg     | 47, 25, 300   | `#776994`       |
findMatchBg         | 35, 25, 180   | `#145d51`       |
findMatchHlBg       | 25, 20, 60    | `#4f3521`       |
listActiveSelBg     | 25, 20, 300   | `#403756`       |
progressBarBg       | 45, 50, 240   | `#0078b3`       |
border              | 20, 5, 60     | `#362f2a`       |
checkboxBorder      | 40, 5, 60     | `#655d57`       |
peekViewBg          | 5, 7, 180     | `#001411`       |
