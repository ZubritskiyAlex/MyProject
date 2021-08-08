import React, { useEffect } from "react";
import axios from "axios";
import {Link, useParams} from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {removeSelectedProduct, selectedProduct} from "../redux/actions/productActions";
import {Button} from "@material-ui/core";


import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import AddShoppingCartRoundedIcon from '@material-ui/icons/AddShoppingCartRounded';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import {makeStyles} from "@material-ui/core/styles";
import AutorenewIcon from '@material-ui/icons/Autorenew';



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




const ProductDetail = () => {
  const classes = useStyles();
  const bull = <span className={classes.bullet}>•</span>;
  const { productId } = useParams();
  let product = useSelector((state) => state.product);
  const { image, title, price, category, description } = product;
  const dispatch = useDispatch();


  const fetchProductDetail = async (id) => {
    const response = await axios
      .get(`https://fakestoreapi.com/products/${id}`)
      .catch((err) => {
        console.log("Err: ", err);
      });
    dispatch(selectedProduct(response.data));
  };

  useEffect(() => {
    if (productId && productId !== "") fetchProductDetail(productId);
    return () => {
      dispatch(removeSelectedProduct());
    };
  }, [productId]);
  return (
    <div className="ui grid container">
      {Object.keys(product).length === 0 ? (
        <div><AutorenewIcon/></div>
      ) : (
          <Card className={classes.root}>
      <CardContent>
        <Typography variant="h5" component="h2">
          {title}
        </Typography>
        <Typography className={classes.pos} color="textSecondary">
          <div className="column lp">
            <img className="ui fluid image" src={image} />
              </div>
        </Typography>
        <Typography variant="body2" component="p">
          {description}
        </Typography>
        <Typography variant="body2" component="p">
          {price}
        </Typography>
        <Typography variant="body2" component="p">
          {category}
        </Typography>
      </CardContent>
      <CardActions>
        <Link to ="/products"> <Button variant="contained" color="primary" >Back to products</Button>&nbsp;</Link>
        <Link to ="#"> <Button variant="contained" color="secondary" >Add to cart <AddShoppingCartRoundedIcon/></Button>&nbsp;</Link>
        </CardActions>
    </Card>

      )}
    </div>
  );
};

export default ProductDetail;


