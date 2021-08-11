import React from "react";
import { Link } from "react-router-dom";
import {useSelector} from "react-redux";

import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles({
  root: {
    minWidth: 275,
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

const ShopComponent = () => {

    const classes = useStyles();
    const bull = <span className={classes.bullet}>•</span>;
    const shops = useSelector((state) =>state.allShops.shops)
    const renderList = shops.results?.map((shop)=>{
        const {id, name, description, owner} = shop;
        return(

            <Card className={classes.root} key={id}>
            <Link to={`/shop/${id}`}>
            <CardContent>

                <Typography variant="h5" component="h2">
                StoreName:&nbsp; {name}
                </Typography>

                <Typography variant="h5" component="h2">
                Description:&nbsp; {description}
                </Typography>
                <Typography variant="body2" component="p">
                  Owner:&nbsp; {owner}
                </Typography>
        </CardContent>
                  <CardActions>
                    <Button size="small" variant="contained" color="secondary" >Learn More</Button>
                  </CardActions>
        </Link>
     </Card>
   );
  });
  return <>{renderList}</>;
};

export default ShopComponent;