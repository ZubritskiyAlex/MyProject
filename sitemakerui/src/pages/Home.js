import React, {Fragment} from "react";
import {Typography} from "@material-ui/core";
import {Grid,  Paper, Container} from "@material-ui/core";
import {ProductForm} from "../components/ProductForm";
import {Products} from "../components/Products";



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
            <Grid item md={6}>
                <Typography variant="h2" align="center" color="textPrimary" gutterBottom>SiteMaker
                <h3>My first project for remarkable people</h3>
            </Typography>
            </Grid>
            </Grid>

        </Container>
    </Paper>
     <ProductForm/>
         <hr/>
         <Products products={products}/>
    </Fragment>

    )

}

export default Home();