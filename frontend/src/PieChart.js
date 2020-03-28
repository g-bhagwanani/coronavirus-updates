import React, { Component } from 'react';
import CanvasJSReact from './canvasjs_assets/canvasjs.react';

var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

class PieChart extends Component {

    constructor(props) {
        super(props);
        this.state = {
            deets : [],
            flask_url : window.location.protocol + '//' + window.location.hostname +":5000/"
        };
    }

    componentDidMount() {

        var countryy = this.props.country;

        fetch(this.state.flask_url + '/getinfo?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            deets: result,
                            dataPoints : [
                                { name: "Active Cases", y: result[1].value, percentage: result[1].extra_val, color: "#0490e8" },
                                { name: "Recovered", y: result[2].value, percentage: result[2].extra_val, color: "#e6c004" },
                                { name: "Deceased", y: result[3].value, percentage: result[3].extra_val, color: "#e60448" }
                            ]
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    componentWillReceiveProps(newProps) {

        var countryy = newProps.country;

        fetch(this.state.flask_url + '/getinfo?country=' + countryy)
            .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            deets: result,
                            dataPoints : [
                                { name: "Active Cases", y: result[1].value, percentage: result[1].extra_val, color: "#0490e8" },
                                { name: "Recovered", y: result[2].value, percentage: result[2].extra_val, color: "#e6c004" },
                                { name: "Deceased", y: result[3].value, percentage: result[3].extra_val, color: "#e60448" }
                            ]
                        });
                    },
                    (error) => {
                        console.log(error);
                    }
                )
    }

    render() {
    
        var stuff = this.state.deets;

        const yo = [
            { name: "Active Cases", y: 486, percentage: 30, color: "#bc00eb" },
            { name: "Recovered", y: 40, percentage: 40, color: "#e85d00" },
            { name: "Deceased", y: 10, percentage: 40, color: "#2ee800" }
        ];

        const options = {
            backgroundColor: "rgba(255, 255, 255, 0.8)",
            animationEnabled: true,
            // exportEnabled: true,
			title: {
				text: "Cases Distribution"
			},
			data: [{
				type: "doughnut",
				showInLegend: true,
				indexLabel: "{name} - {percentage}",
                yValueFormatString: "###,###",
				dataPoints: this.state.dataPoints
			}]
		}

        return (
            <CanvasJSChart options = {options} />
        );
    }

}

export default PieChart;