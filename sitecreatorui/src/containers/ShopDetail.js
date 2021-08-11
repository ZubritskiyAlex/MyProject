import React, { useEffect } from "react";
import axios from "axios";
import {Link, useParams} from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import {removeSelectedShop, selectedShop} from "../redux/actions/shopActions";
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

const ShopDetail = () => {

  const classes = useStyles();
  const bull = <span className={classes.bullet}>•</span>;
  const { shopId } = useParams();
  let shop = useSelector((state) => state.shop);
  const {title, owner, description } = shop;
  const dispatch = useDispatch();

  const fetchShopDetail = async (id) => {
    const response = await axios
      .get(`http://127.0.0.1:8000/api/store/${id}`)
      .catch((err) => {
        console.log("Err: ", err);
      });

    dispatch(selectedShop(response.data));
  };

  useEffect(() => {
    if (shopId && shopId !== "") fetchShopDetail(shopId);
    return () => {
      dispatch(removeSelectedShop());
    };
  }, [shopId]);

  return (
    <div className="ui grid container">
      {Object.keys(shop).length === 0 ? (
        <div>...Loading</div>
      ) : (
          <Card className={classes.root}>
      <CardContent>
        <Typography variant="h5" component="h2">
          {title}
        </Typography>
        <Typography className={classes.pos} color="textSecondary">
          {owner}
        </Typography>
        <Typography variant="body2" component="p">
          {description}
        </Typography>
      </CardContent>
      <CardActions>
        <Link to ="/"><Button variant="contained" color="primary" >Back to shops</Button></Link>
      </CardActions>
    </Card>
      )}
    </div>
  );
};

export default ShopDetail;