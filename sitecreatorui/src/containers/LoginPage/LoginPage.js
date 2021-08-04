import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import {useState} from "react";


export const LoginPage = ({setIsLoggedIn, history, setUserName}) => {

    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');


    const handleLoginChange = (e) => {
        setLogin(e.target.value)
    }

    const handlePasswordChange = (e) =>
    {
        setPassword(e.target.value)
    }

    const handleLogIn = (e) => {
        e.preventDefault()

        localStorage.setItem("isLoggedIn", true);
        localStorage.setItem("userName", login)

        setUserName(login)
        setIsLoggedIn(true)
        history.push('/')
    }




    return (
        <h1>
        <form className="loginForm" onSubmit={handleLogIn}>
            <h2>Authorization</h2>
            <div>
                <input
                    className="loginFormInput"
                    type="text"
                    placeholder="Login"
                    onChange={handleLoginChange}
                    required
                />
            </div>
            <div>
                <input
                    className="loginFormInput"
                    type="password"
                    placeholder="password"
                    onChange={handlePasswordChange}
                    required
                />
            </div>
            <div>
                <button type="submit"> &nbsp;Log in&nbsp;<ExitToAppIcon/></button>
            </div>
        </form>
    </h1>
    );
};