import React from "react";
import {Container, Grid, Paper, Typography} from "@material-ui/core";

export const About = () => {
    return(<div>
        <h1>About app</h1>
            <hr/>
        <Typography variant="h1" align="center" color="textPrimary" gutterBottom>
            <Paper>
        <Container fixed>
            <div/>
            <Grid container>
            <Grid item md={12}>
                <Typography variant="h2" align="center" color="textPrimary" gutterBottom>Welcome to SiteMaker!
                <p>This is my first experience with React!</p>
                <h2>I hope you enjoy it   : )</h2>
            </Typography>
            </Grid>
            </Grid>

        </Container>
            </Paper>

        </Typography>
        </div>






    )

}