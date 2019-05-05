# Changelogs

### Version `0.3`
- Class `Root`
    - Calling methods with invalid widget key will now raise an error.
    - Some methods were renamed to be more memorable.
    - Added method `createRadioGroup`
- Added Class `ViewBase`
    - This class exists for inheritance purposes, no instances should be created
    - Most contents of the `View` class were moved to this one
- Class `View`
    - Class now inherits from new class `ViewBase`
    - Removed `widgets` member variable. It was not utilized.
    - Some methods were renamed to be more memorable.
    - Removed method `addWidget`
    - Removed method `createRadioGroup`
    - Added method `addDialog`
    - Added method `showDialog`
- Added Class `Dialog`
    - Class inherits from `ViewBase`
    - Added method `setEndProtocol`
- Removed `output bool` widget type completely

### Version `0.2`
- Added package guide
- Added package reference

### Version `0.1`
Initial Version of the Package
