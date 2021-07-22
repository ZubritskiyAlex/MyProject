import React from 'react'
import {
    Button, Container, Grid,
    Typography, Card, CardMedia, CardContent, CardActions, makeStyles
} from "@material-ui/core";
import LayerIcon from '@material-ui/icons/Layers'
import PlayCircleFilledIcon from '@material-ui/icons/PlayCircleFilled'


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


const cards = [1,2,3,4,5,6,7,8,9];
function ProductsContent(){
    const classes = useStyles();
    return(
<main>

    <Container className={classes.cardGrid} maxWidth="md">
        <Grid container spacing={4}>
            {cards.map((card) =>(
                <Grid item key={card} xs={12} sm={6} md={4}>
                    <Card className = {card}>
                        <CardMedia
                            className = {classes.cardMedia}
                            image = 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/BMW_logo_%28gray%29.svg/2048px-BMW_logo_%28gray%29.svg.png'
                            title = "Image title"
                                />
                        <CardContent>
                            <Typography variant="h5" gutterBottom>
                                Blog post
                            </Typography>
                            <Typography variant="h5" gutterBottom>
                                Blog postdfamgnsgd snmgndfg HEROTA
                            </Typography>
                        </CardContent>
                        <CardActions>
                            <Button size="small" color="primary">
                                View
                            </Button>
                            <Button size="small" color="primary">
                                Edit
                            </Button>
                        <LayerIcon/>
                        <PlayCircleFilledIcon/>
                        </CardActions>
                    </Card>
                </Grid>


            ))}
        </Grid>
    </Container>
</main>
  )
}
export default ProductsContent;