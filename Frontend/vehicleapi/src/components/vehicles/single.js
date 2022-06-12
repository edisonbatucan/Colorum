import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axios';
import { useParams } from 'react-router-dom';
//MaterialUI
import CssBaseline from '@material-ui/core/CssBaseline';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
}));

export default function Vehicle() {
	const { id } = useParams();
	const classes = useStyles();

	const [data, setData] = useState({ vehicle: [] });

	useEffect(() => {
		axiosInstance.get(id).then((res) => {
			setData({ vehicle: res.data });
			console.log(res.data);
		});
	}, [setData]);

	return (
		<Container component="main" maxWidth="md">
			<CssBaseline />
			<div className={classes.paper}></div>
			<div className={classes.heroContent}>
				<Container maxWidth="sm">
					<Typography
						component="h1"
						variant="h2"
						align="center"
						color="textPrimary"
						gutterBottom
					>
						{data.vehicle.car_name}
					</Typography>
					<Typography
						variant="h4"
						align="center"
						color="textSecondary"
						paragraph
					>
					<strong>Price:</strong> ₱ {data.vehicle.price}
					</Typography>
					<Typography
						variant="h4"
						align="center"
						color="textSecondary"
						paragraph
					>
					<strong>Number of Seats:</strong> {data.vehicle.num_seats}
					</Typography>
					<Typography
						variant="h4"
						align="center"
						color="textSecondary"
						paragraph
					>
					<strong>Wheel Size:</strong> {data.vehicle.wheel_size}
					</Typography>
					<Typography
						variant="h4"
						align="center"
						color="textSecondary"
						paragraph
					>
					<strong >{data.vehicle.car_type}</strong>
					</Typography>
				</Container>
			</div>
		</Container>
	);
}