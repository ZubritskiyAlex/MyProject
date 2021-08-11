import React from "react";
import {Link} from "react-router-dom";
import InfoIcon from "@material-ui/icons/Info";
import ExitToAppIcon from "@material-ui/icons/ExitToApp";
import { Button} from "@material-ui/core";
import StoreIcon from '@material-ui/icons/Store';
import AddBoxIcon from '@material-ui/icons/AddBox';
import AddCircleOutlineOutlinedIcon from '@material-ui/icons/AddCircleOutlineOutlined';
import LocalAtmOutlinedIcon from '@material-ui/icons/LocalAtmOutlined';
import clsx from 'clsx';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';

import MenuIcon from '@material-ui/icons/Menu';
import {HomeRounded} from "@material-ui/icons";



const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  toolbar: {
    paddingRight: 24,
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'flex-end',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  appBar: {
    zIndex: theme.zIndex.drawer + 1,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
  },
  appBarShift: {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  menuButton: {
    marginRight: 36,
  },
  menuButtonHidden: {
    display: 'none',
  },
  title: {
    flexGrow: 1,
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
}));

export default function Dashboard() {
  const classes = useStyles();
  const [open, setOpen] = React.useState(true);
  const handleDrawerOpen = () => {
    setOpen(true);
  };
  const handleDrawerClose = () => {
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <CssBaseline />
        <nav className="navbar navbar-light bg-light">
            <div className="container">
                 <Link to ="/about">
                    <img src="https://opencartforum.com/storage/profile/monthly_2018_11/Compress-Images.png.d4103238b5fac0314c7a4542c488a949.png" alt="logo" width="240" height="60"/>
                 </Link>
            </div>
        </nav>
      <AppBar position="absolute" className={clsx(classes.appBar, open && classes.appBarShift)}>
        <Toolbar className={classes.toolbar}>
          <IconButton
            edge="start"
            color="inherit"
            aria-label="open drawer"
            onClick={handleDrawerOpen}
            className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
          >
            <MenuIcon />
          </IconButton>
          <Typography component="h1" variant="h6" color="black" noWrap className={classes.title}>
            <Link to ="/about"><Button variant="contained" color="primary" > &nbsp;<HomeRounded/>&nbsp; SiteCreator</Button></Link>
          </Typography>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            <Link to ="/products"> <Button variant="contained" color="primary" > &nbsp;<LocalAtmOutlinedIcon/>&nbsp; Products&nbsp;</Button></Link>
          </Typography>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
            <Link to ="/"><Button variant="contained" color="primary" >Shops &nbsp; <StoreIcon />&nbsp;</Button></Link>
          </Typography>

          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
              <Link to ="/addproduct"><Button variant="contained" color="primary" >Create product! &nbsp;<AddCircleOutlineOutlinedIcon/> </Button></Link>
          </Typography>

          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
              <Link to ="/addshop"><Button variant="contained" color="primary" >  &nbsp;Create shop! &nbsp;<AddBoxIcon/> </Button></Link>
          </Typography>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
              <Link to ="/about"><Button variant="contained" color="primary" >About app &nbsp;<InfoIcon/></Button></Link>
          </Typography>
          <Typography component="h1" variant="h6" color="inherit" noWrap className={classes.title}>
             <Link to ="/login"><Button variant="contained" color="primary" >Login &nbsp;<ExitToAppIcon/></Button></Link>
          </Typography>


        </Toolbar>
      </AppBar>
      <Drawer
        variant="permanent"
        classes={{
          paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
        }}
        open={open}
      >
        <div className={classes.toolbarIcon}>

        </div>

      </Drawer>

    </div>
  );
}