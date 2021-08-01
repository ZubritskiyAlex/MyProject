import './ProductCard.css'
import AddShoppingCartOutlinedIcon from '@material-ui/icons/AddShoppingCartOutlined';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';


export const ProductCard = ({ title,
    description,
    price,
    in_cart,
    orderProduct,
    deleteProduct
                            }) => {

    const cartFill = in_cart ? 'crimson': 'black'

        return(
        <div className="post">
            <div className="postContext">
            <h2>{title}</h2>
            <p>{description}</p>
            <p>{price}</p>
                <div>
                <button onClick={orderProduct}>
                    <AddShoppingCartOutlinedIcon style={{fill: cartFill}} />
                </button>
            </div>
        </div>
            <button className="deleteBtn" onClick={deleteProduct}>
                <HighlightOffIcon/>
            </button>
        </div>
    );
};