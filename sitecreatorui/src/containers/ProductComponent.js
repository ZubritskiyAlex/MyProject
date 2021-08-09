import React from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

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

const ProductComponent = () => {
  const classes = useStyles();
  const bull = <span className={classes.bullet}>•</span>;
  const products = useSelector((state) => state.allProducts.products);
  const renderList = products.map((product) => {
    const { id, title, image, price, category } = product;
    return (


        <Card className={classes.root} variant="outlined" key={id}>
        <Link to={`/product/${id}`}>
          <CardContent>
          <Typography className={classes.title} color="textSecondary" gutterBottom>
            {category}
          </Typography>
            <Typography variant="h5" component="h2">
          {title}
        </Typography>

              <Typography className="image">
                <img src={image} alt={title} />
              </Typography>
        <Typography variant="body2" component="p">
              Price: {price}$
        </Typography>
         </CardContent>
          <CardActions>
        <Button variant="contained" color="primary" >About product</Button>&nbsp;
      </CardActions>
        </Link>
     </Card>
    );
  });
  return <>{renderList}</>;
};

export default ProductComponent;
