import {products} from "../../shared/projectData";
import {ProductCard} from "./components/ProductCard";
import {Component} from "react";

export class ProductContent extends Component {

    state = {
        showProducts: true,
        productsArr: JSON.parse(localStorage.getItem('blogProducts'))|| products
    };

    orderProduct = id =>{
        const temp = [...this.state.productsArr];
        temp[id].in_cart = !temp[id].in_cart;

        this.setState({
            productsArr:temp
        })

        localStorage.setItem('blogProducts',JSON.stringify(temp))
   }



    render(){
    const blogProducts = this.state.productsArr.map((item,id) => {
            return (
                <ProductCard
                    id ={item.id}
                    title = {item.title}
                    description = {item.description}
                    price = {item.price}
                    quantityCount={item.quantityCount}
                    orderProduct={() => this.orderProduct(id)}

                />
            );
        }
    )

        return (
            <>
                {
                    <>
                        <h1>Simple ProductCreator</h1>
                        <div className="posts">
                            {blogProducts}
                        </div>
                    </>

                }
            </>
        );

  };
}


