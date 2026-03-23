class ForcedChannelJoinVerificationMiddleware:
    def __init__(self, required_channel_id):
        self.required_channel_id = required_channel_id

    async def __call__(self, request, handler):
        user_channel_id = request.user.channel_id  # Example: Get user's channel ID from the request
        
        if user_channel_id != self.required_channel_id:
            return HTTPForbidden("You must join the required channel to access this resource.")
        
        return await handler(request)  # Proceed to the next middleware or handler