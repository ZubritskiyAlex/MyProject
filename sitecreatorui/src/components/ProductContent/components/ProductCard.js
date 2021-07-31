export const ProductCard = ({ title,
    description,
    price,
    quantityCount,
    orderProduct}) => {


        return(
        <div className="post">
            <h2>{title}</h2>
            <p>{description}</p>
            <p>{price}</p>
            <div>
                <button onClick={orderProduct}>add to card</button>
                {quantityCount}
            </div>
        </div>
    );
};