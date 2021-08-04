import './header.css'
import {Link, NavLink} from 'react-router-dom'
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import InfoIcon from "@material-ui/icons/Info"
import MeetingRoomIcon from "@material-ui/icons/MeetingRoom";


export const Header = ({isLoggedIn, setIsLoggedIn, userName}) => {
    const handleLogOut = () => {
        localStorage.setItem('isLoggedIn', false)
        setIsLoggedIn(false);
    };

    return(
        <header>
            {
                isLoggedIn ?
                    <nav>
                        Hello,&nbsp;<strong>{userName}</strong>
                        <NavLink
                        onClick = {handleLogOut}
                        exact
                        to ="/login"
                        >
                            <MeetingRoomIcon/>
                            Exit
                        </NavLink>
                    </nav>
                : 'Welcome, maybe auth?'
            }

            <nav>
                <Link to ="/products">Products</Link>
                <Link to ="/shops">Shops</Link>
                <Link to ="/productcreate">Create product</Link>
                <Link to ="/shopcreate">Create shop</Link>
                <NavLink to ="/about">About &nbsp;<InfoIcon/></NavLink>
                <Link to ="/login">Login &nbsp; <ExitToAppIcon/></Link>
            </nav>
        < /header>
    );
};