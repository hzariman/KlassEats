<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://upload.wikimedia.org/wikipedia/ms/b/bd/Logo_Alice_Smith_School.png">
    <img src="https://upload.wikimedia.org/wikipedia/ms/b/bd/Logo_Alice_Smith_School.png" alt="Logo" width="160" height="160">
  </a>

<h3 align="center">School Food Booking System Project</h3>

  <p align="center">
    Online ordering system
    <br />
    <a href="https://docs.google.com/document/d/1V3_2wymmc5suPy9miqJc3s3rGwfHhzAKnqZuX5K8ujQ/edit?usp=sharing"><strong>Project Writeup »</strong></a>
    <br />
    <br />
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This Project creates a system uses HTML/CSS and Python (using the Django framework) which allows students to pre-order their meals ahead of time. It contains seperate interfaces for the Admin, Staff and Student users that allow them to perform certain task.

_For more detailed information, please refer to the [Documentation](https://docs.google.com/document/d/1V3_2wymmc5suPy9miqJc3s3rGwfHhzAKnqZuX5K8ujQ/edit?usp=sharing)_



### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

A version of Python (3.7 or later) is required to run the development server. The link for this can be found above. 
It is also important to install the dependencies later after downloading the contents, otherwise the program will not correctly function.
It is highly recommendeded to install these dependencies on a virtual environment such as [Conda](https://docs.conda.io/en/latest/miniconda.html) or VirtualEnv.
  
### Installation

1. Download the file *KlassEats.zip* from [Releases](https://github.com/hzariman/KlassEats/releases/tag/v0.1.0) and navigate to its directory.
2. Within the virtual environment, install the necessary dependencies within the requirements.txt file. This can be done by sending the following command:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the local development server:
   ```sh
   python manage.py runserver
   ```
### Creating User Types
In order to manage different object groups, you must create a superuser via the Django framework. This can be done by entering the following:
 ```sh
   python manage.py createsuperuser
   ```
  Then proceed to enter a desired name and password. Once the server is run, login and navigate to the /admin page to view all registered objects (users and menu items). From there, the admin user is able to assign staff roles to other accounts.
  
  Please note: Creating users through the main website requires an email address ending in '@alice-smith.edu.my' to register.
  <br>For more information, visit the [project writeup](https://docs.google.com/document/d/1V3_2wymmc5suPy9miqJc3s3rGwfHhzAKnqZuX5K8ujQ/edit?usp=sharing)</br>

## Video Demo
A video demo of the website can be found, demonstrating the features that were main targets to implement. This can be found by scanning the QR code below or following this [link](https://youtu.be/ixkiAty3mww).

<div align="center">
  <a href="https://youtu.be/ixkiAty3mww">
    <img src="static/img/klasseatsqr.png" alt="Logo" width="160" height="160">
  </a>
</div>


Please note: the timestamps refer to the different rubic points aimed to be achieved at the end of the [project writeup](https://youtu.be/ixkiAty3mww).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Your Name - Hariz Zariman - hzariman@gmail.com

Project Link: [https://github.com/hzariman/KlassEats](https://github.com/hzariman/KlassEats)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Django Official Documentation]()
* [Bootstrap themes](https://startbootstrap.com/)
* [Python Django Youtube Tutorial](https://www.youtube.com/watch?v=UmljXZIypDc&list=PLLtIxaRk6P3JRiiW1SAV2BLhuuSSCULRn&ab_channel=CoreySchafer)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
