import React, {Fragment} from "react";
import {Typography} from "@material-ui/core";
import {Grid,  Paper, Container} from "@material-ui/core";
import {Products} from "../components/Products";
import {Shops} from "../components/Shops";



export const Home = () => {
    const products = new Array(3)
        .fill("")
        .map((_,i) =>({id:i, title: `Product ${i+1}`}))


    return(
        <Fragment>
        <Paper>
        <Container fixed>
            <div/>
            <Grid container>
            <Grid item md={12}>
                <Typography variant="h2" align="center" color="textPrimary" gutterBottom>SiteMaker
                <h3>My first project for remarkable people</h3>
            </Typography>
            </Grid>
            </Grid>

        </Container>
    </Paper>
         <hr/>

            <Paper>
        <Container fixed>
            <div/>
            <Grid container>
            <Grid item md={12}>
                <Typography variant="h2" align="center" color="textPrimary" gutterBottom>Here you can
                <h1>Create your shop!</h1>
                <h2>Create your product!</h2>
                <h3>Buy product</h3>
                <h4>Login & Registration </h4>
            </Typography>
            </Grid>
            </Grid>

        </Container>
    </Paper>

    </Fragment>

    )

}

export default Home();