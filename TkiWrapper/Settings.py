from Namespace.Namespace import Namespace

# Package settings
Settings = Namespace(
  # Enable log output to stdio
  enableLogs = True,
  # Set minimum log level ('Debug', 'Info', 'Note', 'Warn', 'Error')
  logLevel = 'Note',
  # Enable package warnings
  enableWarnings = True,
)

# Default app style values
Style = Namespace(
  # TTK Theme used by default
  ttkTheme = 'default',
  # Fixed width of all buttons (None = auto width)
  buttonFixedWidth = None,
  # Font families
  fontStdFamily = 'Verdana',
  fontMonoFamily = 'Courier New',
  # Font sizes in various widgets
  FontSize = Namespace(
    TextField = 11,
  ),
  # Colors of various elements
  Colors = Namespace(
    foreground = '#000',
    background = '#CFCFCF',
    disabled = '#AAA',
    largeTextForeground = '#FFF',
    largeTextBackground = '#000',
  ),
)
