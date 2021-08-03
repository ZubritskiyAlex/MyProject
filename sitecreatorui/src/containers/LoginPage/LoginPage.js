import {Button} from "@material-ui/core";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";

export const LoginPage = () => {
    return (
        <h1> Authorization
            <form className="loginForm">
                <div>
                    <input type ="text" placeholder="Login"/>
                </div>

                <div>
                    <input type ="text" placeholder="Password"/>
                </div>

                <div>
                    <Button variant="contained" color="secondary">Log in  &nbsp; <ExitToAppIcon/></Button>
                </div>

            </form>
        </h1>
    )
}