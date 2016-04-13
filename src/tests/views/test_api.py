from app.models import Invitation, TimeProposal
from app.views.api.schema.time_proposals import (
    time_proposals_schema, times_proposals_schema
)
from app.views.api.schema.place_proposals import (
    place_proposal_schema, places_proposal_schema
)

from tests.views.conftest import call_api, assert_notimplemented


def test_invitations_list_get(client, invitation):
    response, data = call_api(client, '/api/invitations')
    assert data['message'][0][0].get('code') == invitation.code


def test_invitations_list_post(client, input_invitation):
    response, data = call_api(
        client, '/api/invitations', method='POST', payload=input_invitation)

    expected = dict([
        ('error', None),
        ('message', {
            'code': data['message'].get('code'),
            'id': data['message'].get('id')
        })
    ])
    assert data == expected
    assert response.status_code == 200


def test_invitations_get(client, invitation):
    inv_id = invitation.id
    response, data = call_api(client, '/api/invitations/%s' % inv_id)
    assert data['message'][0].get('code') == invitation.code
    assert response.status_code == 200


def test_invitations_post(client):
    response, data = call_api(client, '/api/invitations/1212', method='PUT')
    assert_notimplemented(response, data)


def test_invitations_delete(client, invitation):
    inv_id = invitation.id
    response, data = call_api(
        client, '/api/invitations/%s' % inv_id, method='DELETE')
    deleted = Invitation.get_by_id(inv_id)
    assert not deleted
    assert response.status_code == 200


def test_time_proposals_list_get(client, invitation):
    inv_id = invitation.id
    response, data = call_api(
        client, '/api/invitations/%s/time_proposals' % inv_id)
    assert data['message'][0] == times_proposals_schema.dump(
        invitation.time_proposals).data
    assert response.status_code == 200


def test_time_proposals_list_post(client):
    response, data = call_api(
        client, '/api/invitations/1212/time_proposals',
        method='POST')
    assert_notimplemented(response, data)


def test_time_proposals_get(client, time_proposal):
    inv_id = time_proposal.invitation.id
    tproposal_id = time_proposal.id
    response, data = call_api(
        client,
        '/api/invitations/%s/time_proposals/%s' % (inv_id, tproposal_id))
    assert data['message'][0] == time_proposals_schema.dump(time_proposal).data
    assert response.status_code == 200


def test_time_proposals_put_yes(
        client, user, time_proposal, input_time_response):
    inv_id = time_proposal.invitation.id
    tproposal_id = time_proposal.id
    response, data = call_api(
        client,
        '/api/invitations/%s/time_proposals/%s' % (inv_id, tproposal_id),
        method='PUT', payload=input_time_response)
    decision = time_proposal.time_responses[0].decision
    assert decision is not None and decision
    assert len(data['message'][0]['time_responses']) == 1
    assert response.status_code == 200


def test_time_proposals_delete(client, time_proposal):
    inv_id = time_proposal.invitation.id
    tproposal_id = time_proposal.id
    response, data = call_api(
        client,
        '/api/invitations/%s/time_proposals/%s' % ((str(inv_id), str(tproposal_id))),
        method='DELETE')
    deleted = TimeProposal.get_by_id(tproposal_id)
    assert not deleted
    assert response.status_code == 200


def test_place_proposals_list_get(client, invitation):
    inv_id = invitation.id
    response, data = call_api(
        client, '/api/invitations/%s/place_proposals' % inv_id)
    assert data['message'][0] == places_proposal_schema.dump(
        invitation.place_proposals).data
    assert response.status_code == 200


def test_place_proposals_list_post(client):
    response, data = call_api(
        client, '/api/invitations/1212/place_proposals',
        method='POST')
    assert_notimplemented(response, data)


def test_place_proposals_get(client, place_proposal):
    inv_id = place_proposal.invitation.id
    tproposal_id = place_proposal.id
    response, data = call_api(
        client,
        '/api/invitations/%s/place_proposals/%s' % (inv_id, tproposal_id))
    assert data['message'][0] == place_proposal_schema.dump(place_proposal).data
    assert response.status_code == 200


def _test_place_proposals_put(client, place_proposal, user, decision):
    inv_id = place_proposal.invitation.id
    tproposal_id = place_proposal.id
    response, data = call_api(
        client,
        '/api/invitations/%s/place_proposals/%s' % (inv_id, tproposal_id),
        method='PUT',
        payload={
            'us_id': user.id,
            'decision': decision
        }
    )
    assert response.status_code == 200
    assert len(data['message'][0]['place_responses']) == 1
    assert data['message'][0]['place_responses'][0]['decision'] is decision


def test_place_proposals_put_yes(client, place_proposal, user):
    _test_place_proposals_put(client, place_proposal, user, decision=True)


def test_place_proposals_put_no(client, place_proposal, user):
    _test_place_proposals_put(client, place_proposal, user, decision=False)
