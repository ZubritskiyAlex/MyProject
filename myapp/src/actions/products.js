var mockApiData = [
    {
        id:1,
        name: 'Hoodie'
    },
    {
        id:2,
        name: 'Laptop'
    },
    {
        id:3,
        name: 'Mask'
    },




]

export const getProducts = () =>
    dispatch => {
        setTimeout(() => {
            console.log('I got products');
            dispatch({type: 'FETCH_PRODUCTS_SUCCESS', payload: mockApiData})
        }, 2000)
}