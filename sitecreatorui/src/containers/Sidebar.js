import React from "react";
import {Link, NavLink} from "react-router-dom";
import InfoIcon from "@material-ui/icons/Info";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import {BottomNavigation, Button} from "@material-ui/core";
import StoreIcon from '@material-ui/icons/Store';
import AddBoxIcon from '@material-ui/icons/AddBox';
import AddCircleOutlineOutlinedIcon from '@material-ui/icons/AddCircleOutlineOutlined';
import LocalAtmOutlinedIcon from '@material-ui/icons/LocalAtmOutlined';


const Sidebar = () => {

    return(
            <div>
            <BottomNavigation>
                 <main>
                      <span>
                 <Link to ="/products"> <Button variant="contained" color="primary" > &nbsp;<LocalAtmOutlinedIcon/>&nbsp; Products &nbsp;</Button></Link>
                <Link to ="/"><Button variant="contained" color="primary" >Shops &nbsp; <StoreIcon />&nbsp;</Button></Link>
                <Link to ="/productcreate"><Button variant="contained" color="primary" >Create product! &nbsp;<AddCircleOutlineOutlinedIcon/> </Button></Link>
                <Link to ="/shopcreate"><Button variant="contained" color="primary" >  &nbsp;Create shop! &nbsp;<AddBoxIcon/> </Button></Link>
                <Link to ="/about"><Button variant="contained" color="primary" >About app &nbsp;<InfoIcon/></Button></Link>
                <Link to ="/login"><Button variant="contained" color="primary" >Login &nbsp;<ExitToAppIcon/></Button></Link>
                          </span>
                </main>
            </BottomNavigation>
    </div>

    );
};

export default Sidebar;