# url-shortener
## About
A Flask-based URL shortener app with MongoDB integration, allowing users to generate and manage shortened URLs for personal use.

## Table of Contents
- [About](#about)
- [Built With](#built-with)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [License](#license)

## Built With

<td align="center"><img align="center" width="114" height="30" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/></td>
<td align="center" ><img align="center" src="https://img.shields.io/badge/MongoDB-white?style=for-the-badge&logo=mongodb&logoColor=4EA94B"/></td>

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/caglayagmuricerr/url-shortener.git
   ```
2. Install dependencies (see [Dependencies](#dependencies) section).
   
## Dependencies
1. Install Flask:
   ```
    pip install Flask
   ```

2. __AFTER__ installing Flask install Flask-PyMongo:
   ```
   pip install Flask-PyMongo
   ```

## API Reference

- `POST /shorten`: Shortens the url sent in the request body.

## Configuration

Feel free to utilize my database. Alternatively, you can use your own database by replacing username, password and database-name fields in the code.

`mongodb uri format->` 'mongodb+srv://`username`:`password`@cluster.2grovyh.mongodb.net/`database-name`?retryWrites=true&w=majority'

## License
This project is licensed under the [MIT License](LICENSE). 
