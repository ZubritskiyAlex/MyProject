import React from "react";
import {Link} from "react-router-dom";
import InfoIcon from "@material-ui/icons/Info";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import {BottomNavigation, Button} from "@material-ui/core";
import StoreIcon from '@material-ui/icons/Store';
import AddBoxIcon from '@material-ui/icons/AddBox';
import AddCircleOutlineOutlinedIcon from '@material-ui/icons/AddCircleOutlineOutlined';
import LocalAtmOutlinedIcon from '@material-ui/icons/LocalAtmOutlined';
import {MeetingRoom} from "@material-ui/icons";


const Sidebar = ({userName, isLoggedIn, onLogout}) => {

    return(
            <div className="container">
                 <nav className="navbar navbar-dark bg-dark">
                      <div className="container">

                 <Link to ="/products"> <Button variant="contained" color="primary" > &nbsp;<LocalAtmOutlinedIcon/>&nbsp; Products&nbsp;</Button></Link>
                <Link to ="/"><Button variant="contained" color="primary" >Shops &nbsp; <StoreIcon />&nbsp;</Button></Link>
                <Link to ="/addproduct"><Button variant="contained" color="primary" >Create product! &nbsp;<AddCircleOutlineOutlinedIcon/> </Button></Link>
                <Link to ="/addshop"><Button variant="contained" color="primary" >  &nbsp;Create shop! &nbsp;<AddBoxIcon/> </Button></Link>
                <Link to ="/about"><Button variant="contained" color="primary" >About app &nbsp;<InfoIcon/></Button></Link>
                <Link to ="/login"><Button variant="contained" color="primary" >Login &nbsp;<ExitToAppIcon/></Button></Link>

                {isLoggedIn &&
                <h4 className="ml-auto mr-4">
                    <span className="badge badge-pill badge-secondary text-capitalize">
                        Welcome, {userName}
                    </span>

                </h4> }

                          {isLoggedIn &&
                            <Button variant="contained" color="secondary" onClick={onLogout} className="btn btn-outline-warning">
                                Logout |<MeetingRoom/>
                            </Button>

                          }

                 </div>
            </nav>
    </div>

    );
};

export default Sidebar;