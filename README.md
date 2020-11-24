<p align="center">
  <img src="./assets/logo.PNG" width="30%" alt="Logo">
  <h3 align="center">Tired of creating repos manually?</h3>
  <p align="center">Let the robots at Create.It handle that tedious task for you!</p>
  <p align="center">Create.It is a command line interface (CLI) <br />that allows you to create a repository on <br />your favorite git version control platform. <br />Whether that be GitHub or Bitbucket. </p>
  <p align="center">
    <a href="https://github.com/AhadKhan98/Create.It/issues">Report Bug</a>
    ·
    <a href="https://github.com/AhadKhan98/Create.It/issues">Submit Feature</a>
  </p>
</p>
<hr>

## How it Works
Create.It is a CLI made completely using Python. We use a library called click to set up the CLI and make things more clean. Create.It has two required arguments that need to be passed in ```--name``` and ```--mode```.
<br />
The name argument refers to the name of the repository that you wish to create. 
<br />
The mode argument allows you to select either 1 for GitHub or 2 for Bitbucket. 
<br />
<br />
After this step, the robots work in the background to connect to GitHub or Bitbuckets' API and try to authenticate your credentials. Once this is done, all you have to do is check out your newly created repository!

Currently Create.It only supports Bitbucket and Github but we hope to add more version control systems in the future.

## Getting Started

#### Cloning The Repo
1. Make sure you have git installed on your computer.
2. Run the following command to clone the repo: ```git clone https://github.com/AhadKhan98/Create.It.git```

#### Running The Script
1. Browse to the ```scripts``` folder
2. Open a terminal window and run the following command ```python main.py --name="YOUR REPO NAME" --mode=X``` Replace 'X' with either 1 or 2. 1=Github | 2=Bitbucket 
3. You will be asked to authenticate your Github/Bitbucket account.
4. Check out your newly created repo!


*For example, if I wanted to create a repo named my-repo on Bitbucket, I would run the following command:* 
<br />
```python main.py --name="my-repo" --mode=2```

## Contributing
We would absolutely love for you to help us in making Create.It better by contributing to our project. Head to the Contributors page to get started right away!

## Code of Conduct
We promote an open and a welcoming environment in this community. We pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.
Learn more about our [Code of Conduct](https://github.com/AhadKhan98/Create.It/blob/master/CODE-OF-CONDUCT.md).

## Video Demo
Watch our demo on [YouTube](https://google.com/)

## License
[MIT @ MLH Fellowship 2020](https://github.com/AhadKhan98/Create.It/blob/master/LICENSE)

Made with ❤ by [Ahad Zai](https://github.com/ahadkhan98) and [Mondale Felix](https://github.com/MondaleFelix) during MLH Fellowship Explorer Sprint 4 (Fall 2020)
