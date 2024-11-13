# Invoice Management API

## Overview

This project is a simple API built with Django and Django REST Framework (DRF) to manage invoices and their details. It supports creating and updating invoices along with multiple details in a single API call, utilizing nested serializers.

## Project Requirements

### Models

- **Invoice**: Stores invoice information such as `invoice_number`, `customer_name`, and `date`.
- **InvoiceDetail**: Linked to `Invoice`, stores line items with fields like `description`, `quantity`, `price`, and `line_total`.

### API Endpoint

- **Endpoint**: `/api/invoices/`
- **Methods**: 
  - `POST` (create)
  - `PUT` (update)
- **Functionality**: Allows for creating a new invoice with multiple details or updating an existing invoice and replacing its details.

## Setup Instructions

### Prerequisites

- Python 3.12
- Django and Django REST Framework
- Virtual Environment (optional, recommended)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ram-meegada/invoice_project.git
   cd main_project
2. **Create and Activate a Virtual Environment:**

   ```bash
   python3.12 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. pip install -r req.txt
4. python manage.py runserver

## Deployment Overview

The application has been deployed using:

- **Nginx**: Acts as the reverse proxy server to serve the Django application and handle incoming HTTP requests.
- **Gunicorn**: A WSGI HTTP server to run the Django application, providing a high-performance interface between Django and Nginx.
- **Docker**: The application has been containerized using Docker to ensure consistency across environments and simplify the deployment process.
