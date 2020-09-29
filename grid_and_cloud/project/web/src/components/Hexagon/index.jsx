import React from 'react';

import './style.css';


const Online = (props) => {
	const { url } = props

	return (
		<div className="hexagon" id="avatar">
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1">
				<path d="M0.5,0.0005C0.475,0.0005,0.4495,0.005,0.4255,0.0145c-0.038,0.0145-0.091,0.039-0.159,0.0785c-0.068,0.0395-0.1155,0.0735-0.147,0.0994 C0.08,0.2245,0.0535,0.2705,0.0455,0.3215c-0.0065,0.0405-0.012,0.099-0.012,0.179c0,0.079,0.0055,0.1375,0.012,0.178c0.008,0.0515,0.0345,0.0969,0.0745,0.1295 c0.032,0.026,0.079,0.06,0.147,0.0994c0.068,0.0395,0.1215,0.064,0.1595,0.079c0.048,0.0185,0.1005,0.0185,0.148-0.0005c0.038-0.0145,0.091-0.039,0.159-0.079c0.068-0.0395,0.1155-0.0735,0.147-0.0994c0.0395-0.0325,0.0665-0.0785,0.0745-0.1295c0.0065-0.0405,0.012-0.099,0.012-0.179c-0.0005-0.079-0.006-0.1369-0.012-0.178c-0.008-0.0515-0.0345-0.0969-0.0745-0.1295c-0.032-0.026-0.079-0.06-0.147-0.0994C0.665,0.053,0.612,0.0285,0.574,0.0139C0.55,0.005,0.525,0.0005,0.5,0.0005z" fill={`url(#${url})`} />
				<defs>
					<pattern id={url} x="0" y="0" width="1" height="1" viewBox="0 0 1 1">
						<rect x="0" y="-0.035" />
						<image xlinkHref={url} x="-0.035" width="1.07" height="1.07" y="-0.035" preserveAspectRatio="xMidYMid slice" />
					</pattern>
				</defs>
			</svg>
		</div>
	);
};

export default Online;