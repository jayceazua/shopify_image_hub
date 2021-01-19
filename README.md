# Shopify Image Hub 
Shopify Challenge Backend Internship 2021 
<br/>

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/jayceazua/shopify_image_hub/commits/main)
[![Website shields.io](https://img.shields.io/website-up-down-green-red/http/shields.io.svg)](https://shopify-image-hub-2021.herokuapp.com/)
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://github.com/jayceazua/shopify_image_hub/issues)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)



## How to Use App
1. Follow the [Live Link here](https://shopify-image-hub-2021.herokuapp.com/)
2. Create an account
3. Upload and share your favorite images
4. Search for your favorite images

## Current Features

| Features                                   | Done ️   |
| ------------------------------------------ | :------:  |
| A user can create an account               |     ☑     |
| A user can login into their account        |     ☑     |
| A user can logout of their account         |     ☑     |
| Only a user can add images to the repo     |     ☑     |
| Users can only delete their images         |     ☑     |
| Anyone can search for images               |     ☑     |
| Details page has a related images feature  |     ☑     |

## Images API

| Methods    | Urls                | Actions              | Done |
|  :------:  |  :------:           |  :------:            | :-----:|
| GET        | `/items`            | get all Images       | ☑ |
| GET        | `/items/:id`        | get Image by `id`    | ☑ |
| DELETE     | `/items/:id/delete` | remove Image by `id` | ☑ |
| PATCH      | `/items/:id/update` | update Image by `id` |   |

## Tech Stack
- PostgreSQL
- Django
- Python
- Jinja Templating Engine
- AWS

## Entity Relation Diagram
![Entity Relation Diagram](erd.png)

