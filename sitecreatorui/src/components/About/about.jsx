import {Typography} from "@material-ui/core";
import GitHubIcon from '@material-ui/icons/GitHub';
import TelegramIcon from "@material-ui/icons/Telegram";
import LinkedInIcon from "@material-ui/icons/LinkedIn";
import InstagramIcon from "@material-ui/icons/Instagram";


import {Link} from 'react-router-dom';
export const About = () => {

    return(
        <Typography>

            <div>
                <h1>About App</h1>
                <h2>Hello, I am happy to see you here! </h2>
                <pre>
                    On this site you can create your own store with any goods, also you can
                    create products.
                    This is my first experience with React, I hope you will appreciate it :)



                </pre>
                <Link href="#">
                    <h2>You can find the source code here <GitHubIcon/></h2>
                </Link>
                    <h3>
                        Also I will also be glad to hear criticism and suggestions
                    </h3>

                <Link href="#">LinkedIn: &nbsp; <LinkedInIcon/></Link>
                <Link href="#"> Telegram: &nbsp;<TelegramIcon/></Link>
                <Link href="#"> Instagram: &nbsp;<InstagramIcon/></Link>
            </div>
        </Typography>
    );
};




