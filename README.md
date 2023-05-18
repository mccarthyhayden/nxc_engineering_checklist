# nxc_engineering_checklist

This custom module was developed for Next Chapter Manufacturing to prompt users with engineering checklists on Manufacturing Orders. The addon includes stop-gates to prevent order confirmation prior to checklists completion.

## Features
- Creates 3 new tabs in the mrp.production model (Design Checklist, Design Build Checklist, & Product Configuration Checklist).
- Adds a status indicator to the manufacturing order to indicate checklist completion status.
- Prevents order confirmation prior to checklists completion.
- Posts warning message in chatter when a user attempts to confirm a manufacturing order prior to checklist completion.

## Installation
To install this module, you can use the following steps:

1. Copy this directory to addons folder.
2. Allow Odoo server to restart.
3. Go to Apps.
4. Click 'update apps list' button.
5. Clear search filter and search for this addon.
6. Click Install.

## Usage
To use this module, you can follow these steps:

1. Go to Manufacturing > Operations > Manufacturing Orders.
2. Click Create.
3. Complete the 'Design' checklist.
4. Complete the 'Design Build' checklist.
5. Toggle the internal and customer design approvals.
6. Complete the 'Product Configuration' checklist.
7. When the checklists are completed, you be permitted to confirm the order.

## Support
If you have any questions or problems with this module, please contact the author at haydenmccarthy19@gmail.com