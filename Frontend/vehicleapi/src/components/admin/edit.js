import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axios';
import { useHistory, useParams } from 'react-router-dom';
//MaterialUI
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	form: {
		width: '100%', // Fix IE 11 issue.
		marginTop: theme.spacing(3),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}));

export default function Create() {
	const history = useHistory();
	const { id } = useParams();
	const initialFormData = Object.freeze({
		id: '',
		car_name: '',
		price: '',
		num_seats: '',
		wheel_size: '',
		car_type: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	useEffect(() => {
		axiosInstance.get('admin/edit/vehicledetail/' + id).then((res) => {
			updateFormData({
				...formData,
				['car_name']: res.data.car_name,
				['price']: res.data.price,
				['num_seats']: res.data.num_seats,
				['wheel_size']: res.data.wheel_size,
				['car_type']: res.data.car_type
			});
			console.log(res.data);
		});
	}, [updateFormData]);

	const handleChange = (e) => {
		updateFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);

		axiosInstance.put(`admin/edit/` + id + '/', {
			car_name: formData.car_name,
			price: formData.price,
			person: 2,
			num_seats: formData.num_seats,
			wheel_size: formData.wheel_size,
			car_type: formData.car_type,
		});
		history.push({
			pathname: '/admin/',
		});
		window.location.reload();
	};

	const classes = useStyles();

	return (
		<Container component="main" maxWidth="sm">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
					Edit Vehicle
				</Typography>
				<form className={classes.form} noValidate>
					<Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="car_name"
								label="Vehicle Name (String)"
								name="car_name"
								autoComplete="car_name"
								value={formData.car_name}
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="price"
								label="Price (Integer)"
								name="price"
								autoComplete="price"
								value={formData.price}
								type={"number"}
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="num_seats"
								label="Number of Seats (Integer)"
								name="num_seats"
								autoComplete="num_seats"
								value={formData.num_seats}
								type={"number"}
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="wheel_size"
								label="Wheel Size (String: Ex: '18 in - 20 in')"
								name="wheel_size"
								autoComplete="wheel_size"
								value={formData.wheel_size}
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="car_type"
								label="Car Type (suv, pickup, van, sports car)"
								name="car_type"
								autoComplete="car_type"
								value={formData.car_type}
								onChange={handleChange}
							/>
						</Grid>
					</Grid>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						color="primary"
						className={classes.submit}
						onClick={handleSubmit}
					>
						Update Vehicle
					</Button>
				</form>
			</div>
		</Container>
	);
}