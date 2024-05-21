import React, { useState, ChangeEvent, FormEvent } from 'react';
import {
    Container,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableRow,
    TextField,
    Button,
    Alert,
    CircularProgress,
    Box
} from '@mui/material';
import axios from 'axios';
import AdbIcon from '@mui/icons-material/Adb';

const VB12 = () => {
    const [yValues, setYValues] = useState<string[]>(Array(9).fill(''));
    const [error, setError] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);
    const [graphUrl, setGraphUrl] = useState<string>('');

    const handleChange = (index: number, value: string) => {
        const newYValues = [...yValues];
        newYValues[index] = value;
        setYValues(newYValues);
    };

    const handleSubmit = async (event: FormEvent) => {
        event.preventDefault();
        setError(null);
        setLoading(true);
        setGraphUrl('');
        const yValuesNumber = yValues.map(Number);
        if (yValuesNumber.some(isNaN)) {
            setError('All y values must be numbers');
            setLoading(false);
            return;
        }

        try {
            const response = await axios.post('https://api.ikeda042api.net/api/lab/vb12', { y: yValuesNumber });
            setGraphUrl(`https://api.ikeda042api.net/api/lab/lab_files/${response.data.graph_id}`);
        } catch (error: any) {
            setError(error.response ? error.response.data.error : 'An unexpected error occurred');
        } finally {
            setLoading(false);
        }
    };
    return (
        <Container>
            <Typography variant="h4" gutterBottom>VB12 Calibration Curve</Typography>
            <form onSubmit={handleSubmit}>
                <Table>
                    <TableHead>
                        <TableRow>
                            <TableCell align="center" style={{ width: '50%' }}>X</TableCell>
                            <TableCell align="center" style={{ width: '50%' }}>Y</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {yValues.map((value, index) => (
                            <TableRow key={index}>
                                <TableCell align="center">{[0, 0.1, 0.25, 0.5, 1, 2, 2.5, 4, 5][index]}</TableCell>
                                <TableCell align="center">
                                    <TextField
                                        type="number"
                                        value={value}
                                        onChange={(e: ChangeEvent<HTMLInputElement>) => handleChange(index, e.target.value)}
                                        required
                                        fullWidth
                                    />
                                </TableCell>
                            </TableRow>
                        ))}
                    </TableBody>
                </Table>
                <Box display="flex" justifyContent="center" marginTop={2}>
                    <Button type="submit" variant="contained" disabled={loading} startIcon={<AdbIcon />} sx={{ backgroundColor: '#000', color: '#fff' }}>
                        検量線を作成する
                    </Button>
                </Box>
                <Box display="flex" justifyContent="center" marginTop={2}>
                    {loading && <CircularProgress />}
                </Box>
            </form>
            {error && <Alert severity="error">{error}</Alert>}
            {graphUrl && (
                <div>
                    <img src={graphUrl} alt="Graph" style={{ maxWidth: '100%' }} />
                </div>
            )}
        </Container>
    );
};

export default VB12;
