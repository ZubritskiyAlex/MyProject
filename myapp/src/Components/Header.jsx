import React from "react";
import {
    AppBar,
    Container,
    Button,
    IconButton,
    Toolbar,
    Typography,
    Box,
    Paper,
    Grid, Dialog, DialogTitle,
    DialogContentText, TextField, DialogActions, DialogContent,

} from "@material-ui/core";
import {makeStyles} from "@material-ui/core";
import {Link} from "react-router-dom";




const useStyles = makeStyles((theme) => ({
   root: {
       flexGrow:1
   },
    menuButton: {
       marginRight: theme.spacing(1)
   },
    title: {
       flexGrow:1
    },

    mainFeaturesPost:{
       position: "relative",
       color: theme.palette.common.white,
       marginBottom: theme.spacing(4),
       backgroundSize: "cover",
       backgroundRepeat: "no-repeat",
       backgroundPosition: "center"
    },
    overlay:{
      position: "absolute",
      top: 0,
      bottom: 0,
      right: 0,
      left: 0,
      backgroundOverlay: "rgba(0,0,0.3)"

    },
    mainFeaturesPostContent:{
       position: "relative",
       padding: theme.spacing(6),
       marginTop: theme.spacing(8)
    },
    cardMedia: {
       paddingTop: "56.25%"
    }

}))


function Header(){
    const classes = useStyles();

    const [open, setOpen]= React.useState(false);

const handleClickOpen = () =>{
    setOpen(true);
}

const handleClose = () =>{
    setOpen(false);
}

const [opensignup,setOpenSignUp] = React.useState(false);

const handleClickOpenSignUp = () => {
    setOpenSignUp(true);

}

const handleCloseSignUp = () =>{
    setOpenSignUp(false);
}





    return (
        <nav className='app-wrapper'>
            <header className='header'>
            </header>
       <ul>
    <AppBar position="static">
  <Toolbar>
    <IconButton edge="start"
                color="inherit"
                aria-label="menu"
                className={classes.menuButton}
    >

    </IconButton>
    <Typography variant="h6" className={classes.title}>
      My study project
    </Typography>
    <Box mr={3}>
            <Button color="default" variant="contained" onClick={handleClickOpen}>Log In</Button>
            <Dialog open={open} onClose={handleClose} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">Log in</DialogTitle>
                <DialogContent>
                <DialogContent>
                <DialogContentText>
                        Log in to start creating!
                    </DialogContentText>
                </DialogContent>
                <TextField
                    autoFocus
                    margin = "dense"
                    id="name"
                    label= "Email adress"
                    type="email"
                    fullWidth
                />

                 <TextField
                    autoFocus
                    margin = "dense"
                    id="pass"
                    label= "Password"
                    type="password"
                    fullWidth
                />
                </DialogContent>
        <DialogActions>
            <Button onClick={handleClose} color="primary">Log in</Button>
            <Button onClick={handleClose} color="primary">Cancel</Button>
        </DialogActions>
    </Dialog>
    </Box>
      <Box mr={3}>
            <Button color="secondary" variant="contained" onClick={handleClickOpenSignUp} >Sign up</Button>
            <Dialog open={opensignup} onClose={handleCloseSignUp} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">Sign up</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Sign up to start create!
                    </DialogContentText>
                    <TextField
                    autoFocus
                    margin = "dense"
                    id="name"
                    label= "Nickname"
                    type="nickname"
                    fullWidth
                />

                    <TextField
                    autoFocus
                    margin = "dense"
                    id="pass"
                    label= "Password"
                    type="password"
                    fullWidth
                />
                </DialogContent>
            <DialogActions>
                <Button onClick={handleCloseSignUp} color="primary">Cancel</Button>
                <Button onClick={handleCloseSignUp} color="primary">Sign Up</Button>

            </DialogActions>
            </Dialog>
            </Box>

  </Toolbar>
</AppBar>
<main>
    <Button href="#text-buttons" color="primary">Home</Button>

    <Button href="#text-buttons" color="primary">Shops</Button>

    <Link to="/products">
    <Button href="#text-buttons" color="primary">Products</Button>
    </Link>


    <Button href="#text-buttons" color="primary">Create store!</Button>

    <Link to="/createproduct">
    <Button href="#text-buttons" color="primary">Create product!</Button>
    </Link>
    <Button href="#text-buttons" color="primary">Cart</Button>

    <Paper className={classes.mainFeaturesPost}
    style={{backgroundImage: `url(https://cdn6.f-cdn.com/contestentries/876265/6694231/5870d18b44bcb_thumb900.jpg)`}}>
        <Container fixed>
            <div className={classes.overlay}/>
            <Grid container>
            <Grid item md={6}>
                <div className={classes.mainFeaturesPostContent}>
                    <Typography
                     component='h1'
                     variant="h3"
                     gutterBottom
                    >

                    </Typography>
                    <Typography
                        variant='h5'
                        color='inherit'
                        paragraph
                    >
                    </Typography>
                </div>
            </Grid>
            </Grid>

        </Container>
    </Paper>

<div className={classes.mainContent}>
    <Container maxWidth="sm">
        <Typography variant="h2" align="center" color="textPrimary" gutterBottom>Welcome to shop creator!</Typography>
        <Typography variant="h5" align="center" color="textSecondary" paragraph>This is my first website for remarkable people, on it you can create a product, an online store, buy a product and much more. I hope you like it!</Typography>

        <div className={classes.mainButtons}>
            <Grid container spacing={5} justify="center">
                <Grid item>
                    <Link to="/products">
                    <Button variant="contained" color='primary'>Start Now</Button>
                    </Link>
                </Grid>
                <Grid item>
                    <Button variant="outlined" color="primary">Learn more</Button>
                </Grid>
            </Grid>
        </div>
    </Container>
    </div>
</main>
    </ul>
       </nav>
    );
}
export default Header;

