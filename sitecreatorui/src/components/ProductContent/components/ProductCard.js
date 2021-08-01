import AddShoppingCartOutlinedIcon from '@material-ui/icons/AddShoppingCartOutlined';

export const ProductCard = ({ title,
    description,
    price,
    in_cart,
    orderProduct}) => {

    const cartFill = in_cart ? 'crimson': 'black'

        return(
        <div className="post">
            <h2>{title}</h2>
            <p>{description}</p>
            <p>{price}</p>
            <div>
                <button onClick={orderProduct}>
                    <AddShoppingCartOutlinedIcon style={{fill: cartFill}} />
                </button>
            </div>
        </div>
    );
};