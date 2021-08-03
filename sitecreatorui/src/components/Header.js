import './header.css'
import {NavLink} from 'react-router-dom'

export const Header = () => {
    return(
        <header>
            <nav>
                <NavLink exact to="/">
                    Products
                </NavLink>
                <NavLink to="/login">
                    Login
                </NavLink>

            </nav>
        </header>
    )
}