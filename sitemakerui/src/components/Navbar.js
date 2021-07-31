import React from "react";
import {NavLink} from "react-router-dom";

export const Navbar = () => (
    <nav className="navbar navbar-dark navbar-expand-lg bg-success">
        <div className="navbar-brand">
                <NavLink
                   className="nav-link"
                   to = "/"
                   exact
                >
                    SiteMaker
                    (Homepage)
                </NavLink>

        </div>
        <ul className="navbar-nav">



            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/shops"
                   exact
                >
                    Shops
                </NavLink>
            </li>

            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/products"
                   exact
                >
                    Products
                </NavLink>
            </li>


            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/createproduct"
                   exact
                >
                    Create product!
                </NavLink>
            </li>


            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/createshop"
                   exact
                >
                    Create shop!
                </NavLink>
            </li>

            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/about"
                   exact
                >
                    About
                </NavLink>
            </li>



            <li className="nav-item">
                <NavLink
                   className="nav-link"
                   to = "/about"
                   exact
                >
                    Cart
                </NavLink>
            </li>





        </ul>



    </nav>
)