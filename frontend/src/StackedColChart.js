import React, { Component } from 'react';
import CanvasJSReact from './canvasjs_assets/canvasjs.react';

var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class StackedColChart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            activeDataPoints : [],
            recoveredDataPoints : [],
            deathDataPoints : [],
            flask_url : window.location.protocol + '//' + window.location.hostname +":5000/"
        };
    }

    componentDidMount() {

        var countryy = this.props.country;

        fetch(this.state.flask_url + '/gethistory?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            activeDataPoints : result.active,
                            recoveredDataPoints : result.recovered,
                            deathDataPoints : result.deaths
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    componentWillReceiveProps(newProps) {

        var countryy = newProps.country;

        fetch(this.state.flask_url + '/gethistory?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            activeDataPoints : result.active,
                            recoveredDataPoints : result.recovered,
                            deathDataPoints : result.deaths
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    render() {

		const options = {
            backgroundColor: "rgba(255, 255, 255, 0.8)",
			animationEnabled: true,
			title: {
				text: "Change in number of cases over the days"
			},
			toolTip: {
				shared: true
			},
			data: [
			{
				type: "stackedColumn",
				name: "Active Cases",
				showInLegend: true,
				yValueFormatString: "#,###",
				dataPoints: this.state.activeDataPoints
			},
			{
				type: "stackedColumn",
				name: "Recovered Cases",
				showInLegend: true,
				yValueFormatString: "#,###",
				dataPoints: this.state.recoveredDataPoints
			},
			{
				type: "stackedColumn",
				name: "Deaths",
				showInLegend: true,
				yValueFormatString: "#,###",
				dataPoints: this.state.deathDataPoints
			}]
		}

        return (
            <CanvasJSChart options = {options} />
        );
    }

}

export default StackedColChart;