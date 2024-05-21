import { Typography } from '@mui/material';
import { Box } from '@mui/system';

export default function TopPage() {
    return (
        <Box sx={{ bgcolor: "#f7f6f5", color: 'black', minHeight: '100vh' }}>
            <Typography variant="h1" align="center" sx={{ paddingTop: '20vh' }}>
                テスト
            </Typography>
        </Box>
    );
}