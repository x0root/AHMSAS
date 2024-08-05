<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Pixelcraftch/AHMSAS">
  </a>

  <h3 align="center">AHMSAS</h3>

  <p align="center">
    Automated HTTP Method Scanner And Smuggler
    <br />
    <br />
    <br>
    <img alt="Static Badge" src="https://img.shields.io/badge/Made_with-Python-blue"> <img alt="Static Badge" src="https://img.shields.io/badge/Status-Beta-orange"> 
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

Automated HTTP Method Scanner And Smuggler is a powerful and advanced tool designed to test and analyze the security of web applications by sending requests using various HTTP methods. This tool not only highlights the response status codes but also attempts to bypass HTTP restrictions using sophisticated request smuggling techniques. It is an essential utility for security researchers and penetration testers aiming to uncover potential vulnerabilities in web applications.

## Features
- Comprehensive HTTP Method Scanning: Automatically sends requests using multiple HTTP methods (GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH) and highlights the response status codes using colorama for clear 
  visibility.
- Connection Testing: Ensures the target host is reachable before initiating the scan, with multiple retry attempts for robust connectivity checks.
  Request Smuggling: Attempts to bypass 403 Forbidden responses by smuggling requests using various headers. If initial attempts fail, it prompts the user to extend the injection level for more advanced smuggling 
  techniques.
- HTTP Pollution Detection: Checks for potential HTTP pollution vulnerabilities and prompts the user for further scanning if detected.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Pixelcraftch/AHMSAS
   ```
2. Change directory
   ```sh
   cd AHMSAS
   ```
3. Run it
   ```sh
   python3 Ahmsas.py
   ```

<!-- LICENSE -->
## License

Distributed under the Apache-2.0 license License. See `LICENSE` for more information.

