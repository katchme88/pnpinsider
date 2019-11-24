import React from 'react';
import wordcloud from '../wordcloud.png'
import {Card, Container, CardDeck} from 'react-bootstrap'

class Home extends React.Component {
    getStats = (data) => {
        let invites=0;
        let maxScore=0;
        let minScore=0;
        let scoreArray = []

        for (let i=0; i<data.length; i++){
            invites+=parseInt(data[i].invitations)
            scoreArray.push(data[i].score)
        }

        scoreArray = scoreArray.sort()
        minScore = scoreArray[0]
        maxScore = scoreArray[scoreArray.length-1]

        return([invites.toString(), minScore.toString(), maxScore.toString()])
    }

    render() {

        let invites,minScore,maxScore = '';
        if (this.props.data.length>0){
            let stats = this.getStats(this.props.data);
            invites = stats[0]
            minScore = stats[1]
            maxScore = stats[2] 
        }

        return (
            <Container>
                <img src={wordcloud} className="img-fluid" alt="word cloud" />
                <CardDeck>
                <Card border="info" className='text-center'>
                    <Card.Header><b>Total Invites</b></Card.Header>
                    <Card.Body>
                    <Card.Text>
                        {invites}
                    </Card.Text>
                    </Card.Body>
                    <Card.Footer>
                    <small className="text-muted">Last Updated: Today</small>
                    </Card.Footer>
                </Card>
                <Card border="info" className='text-center'>
                    
                    <Card.Header><b>Minimum Score</b></Card.Header>
                    <Card.Body>
                    <Card.Text>
                        {minScore}
                    </Card.Text>
                    </Card.Body>
                    <Card.Footer>
                    <small className="text-muted">Last Updated: Today</small>
                    </Card.Footer>
                </Card>
                <Card border="info" className='text-center'>
                    <Card.Header ><b>Max Score</b></Card.Header>
                    <Card.Body>
                    <Card.Text>
                        {maxScore}
                    </Card.Text>
                    </Card.Body>
                    <Card.Footer>
                    <small className="text-muted">Last Updated: Today</small>
                    </Card.Footer>
                </Card>
                </CardDeck>
            </Container>
        );
    }
}

export default Home;
