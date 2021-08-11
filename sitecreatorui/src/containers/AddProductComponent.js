import React, {Component} from 'react';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import StorefrontIcon from '@material-ui/icons/Storefront';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';


class AddProductForm extends Component{
  constructor(props) {
    super(props)
    this.state = {title: '',
      description: '',
      owner: '',
      store: '',
      price: '',
      category: '',
      items: []
    }
    this.handleDescriptionChange = this.handleDescriptionChange.bind(this);
    this.handleTitleChange = this.handleTitleChange.bind(this);
    this.handleOwnerChange = this.handleOwnerChange.bind(this);
    this.handlePriceChange = this.handlePriceChange.bind(this);
    this.handleCategoryChange = this.handleCategoryChange.bind(this);
    this.handleStoreChange = this.handleStoreChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);


  }

  handleSubmit(event){
   alert('A product'+ this.state.title + 'was been created')
    event.preventDefault();
   this.setState({
     title: event.target.value,
     description: event.target.value,
     owner: event.target.value,
     price: event.target.value,
     category: event.target.value,
     store: event.target.value,
   })


  }

  handleDescriptionChange(event){
    this.setState({description: event.target.value});
  }

  handleTitleChange(event){
    this.setState({title: event.target.value});
  }

  handleOwnerChange(event){
    this.setState({owner: event.target.value})
  }

  handlePriceChange(event){
    this.setState({price: event.target.value})
  }

  handleCategoryChange(event){
    this.setState({category: event.target.value})
  }

  handleStoreChange(event){
    this.setState({store: event.target.value})
  }



  render() {
  return (
      <Container component="main" maxWidth="xs">
      <CssBaseline />
      <div>
        <Avatar>
          <StorefrontIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Create product!
        </Typography>
        <form  onSubmit={this.handleSubmit}>
          <Grid container spacing={2}>
            <Grid item xs={12} sm={6}>
              <TextField
                autoComplete="title"
                name="title"
                variant="outlined"
                required
                fullWidth
                id="title"
                label="Title"
                value={this.state.title}
                onChange={this.handleTitleChange}
                autoFocus
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="Store"
                label="Store"
                name="Store"
                autoComplete="store"
                value={this.state.store}
                onChange={this.handleStoreChange}

              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="description"
                label="Description"
                name="description"
                autoComplete="description"
                value={this.state.description}
                onChange={this.handleDescriptionChange}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                id="price"
                label="Price"
                name="price"
                autoComplete="price"
                value={this.state.price}
                onChange={this.handlePriceChange}
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                variant="outlined"
                required
                fullWidth
                name="category"
                label="Category"
                type="category"
                id="category"
                autoComplete="current-password"
                value={this.state.category}
                onChange={this.handleCategoryChange}
              />
            </Grid>
            <Grid item xs={12}>

            </Grid>
          </Grid>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"

          >
            Create product!
          </Button>
          <Grid container justifyContent="flex-end">
            <Grid item>

            </Grid>
          </Grid>
        </form>
      </div>

    </Container>
  );
}}

export default AddProductForm;