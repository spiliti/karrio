import strawberry
from strawberry.types import Info

import karrio.server.graph.utils as utils
import karrio.server.graph.schemas.base as base
import karrio.server.admin.schemas.tenants.mutations as mutations
import karrio.server.admin.schemas.tenants.inputs as inputs
import karrio.server.admin.schemas.tenants.types as types

extra_types: list = []


@strawberry.type
class Query:
    tenant: types.TenantType = strawberry.field(resolver=types.TenantType.resolve)
    tenants: utils.Connection[types.TenantType] = strawberry.field(
        resolver=types.TenantType.resolve_list
    )


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_tenant(
        self, info: Info, input: inputs.CreateTenantMutationInput
    ) -> mutations.CreateTenantMutation:
        return mutations.CreateTenantMutation.mutate(info, **input.to_dict())

    @strawberry.mutation
    def update_tenant(
        self, info: Info, input: inputs.UpdateTenantMutationInput
    ) -> mutations.UpdateTenantMutation:
        return mutations.UpdateTenantMutation.mutate(info, **input.to_dict())

    @strawberry.mutation
    def delete_tenant(
        self, info: Info, input: inputs.DeleteTenantMutationInput
    ) -> base.mutations.DeleteMutation:
        return mutations.DeleteTenantMutation.mutate(info, **input.to_dict())

    @strawberry.mutation
    def add_custom_domain(
        self, info: Info, input: inputs.AddCustomDomainMutationInput
    ) -> mutations.AddCustomDomainMutation:
        return mutations.AddCustomDomainMutation.mutate(info, **input.to_dict())

    @strawberry.mutation
    def update_custom_domain(
        self, info: Info, input: inputs.UpdateCustomDomainMutationInput
    ) -> mutations.UpdateCustomDomainMutation:
        return mutations.UpdateCustomDomainMutation.mutate(info, **input.to_dict())

    @strawberry.mutation
    def delete_custom_domain(
        self, info: Info, input: inputs.DeleteCustomDomainMutationInput
    ) -> mutations.DeleteCustomDomainMutation:
        return mutations.DeleteCustomDomainMutation.mutate(info, **input.to_dict())
