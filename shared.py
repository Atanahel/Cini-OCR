RECTO_SUBSTRING = '_recto.cr2'
VERSO_SUBSTRING = '_verso.cr2'
SAMPLES_DIR = 'samples'

# IMAGE AND TEXT SECTION CROPPING
ACCEPTABLE_TEXT_SECTIONS_Y_RANGES = [(120, 160), (230, 280)]
RESIZE_HEIGHT = 1000.0
IMAGE_HEIGHT_LIMIT = 0.9 * RESIZE_HEIGHT
IMAGE_WIDTH_DELIMITER = 0.05 * RESIZE_HEIGHT
IMAGE_MASK_BORDER_WIDTH = 15

# CARDBOARD CROPPING
CARDBOARD_MIN_WIDTH = 4550
CARDBOARD_MAX_WIDTH = 4650

CARDBOARD_MIN_HEIGHT = 5100
CARDBOARD_MAX_HEIGHT = 5250

CARDBOARD_MIN_RATIO = 1.11
CARDBOARD_MAX_RATIO = 1.14

