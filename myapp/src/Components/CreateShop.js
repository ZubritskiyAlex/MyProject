
import React from "react";

class CreateShop extends React.Component {
  state = {
    name: "",
    description: "",
    owner: "",
  };

  create = (e) => {
    e.preventDefault();
    if (this.state.name === "" || this.state.description === ""|| this.state.owner === "") {
      alert("ALl the fields are mandatory!");
      return;
    }
    this.props.createShopHandler(this.state);
    this.setState({ name: "", description: "",owner: "" });
    this.props.history.push("/");
  };
  render() {
    return (
      <div className="ui main">
        <h2>Add Contact</h2>
        <form className="ui form" onSubmit={this.create}>
          <div className="field">
            <label>Name</label>
            <input
              type="text"
              name="name"
              placeholder="Name"
              value={this.state.name}
              onChange={(e) => this.setState({ name: e.target.value })}
            />
          </div>
          <div className="field">
            <label>Description</label>
            <input
              type="text"
              name="email"
              placeholder="Email"
              value={this.state.email}
              onChange={(e) => this.setState({ description: e.target.value })}
            />
          </div>

            <div className="field">
            <label>Owner</label>
            <input
              type="text"
              name="email"
              placeholder="Email"
              value={this.state.email}
              onChange={(e) => this.setState({ owner: e.target.value })}
            />
          </div>
          <button className="ui button blue">Create Shop! </button>
        </form>
      </div>
    );
  }
}

export default CreateShop;