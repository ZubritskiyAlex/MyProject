import './ProductCard.css'
import AddShoppingCartOutlinedIcon from '@material-ui/icons/AddShoppingCartOutlined';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';
import EditIcon from '@material-ui/icons/Edit';

export const ProductCard = ({ title,
    description,
    price,
    in_cart,
    orderProduct,
    deleteProduct,
    handleEditFormShow,
    handleSelectProduct
                            }) => {

    const showEditForm = () => {
        handleSelectProduct();
        handleEditFormShow();
    }


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
            <div className="productControl">

                <button className="editBtn" onClick={showEditForm}>
                <EditIcon/>
                </button>
                <button className="deleteBtn" onClick={deleteProduct}>
                    <HighlightOffIcon/>
                </button>
            </div>

        </div>
    );
};