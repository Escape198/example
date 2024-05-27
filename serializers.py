from rest_framework import serializers

class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = ['id', 'attached_file']

class OrderSerializer(serializers.ModelSerializer):
    attached_files = AttachedFileSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'email', 'attached_files']

class OrderCreateSerializer(serializers.ModelSerializer):
    attached_files = serializers.ListField(
        child=serializers.FileField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Order
        fields = ['email', 'attached_files']

    def create(self, validated_data):
        attached_files = validated_data.pop('attached_files', [])
        order = Order.objects.create(**validated_data)
        for file in attached_files:
            AttachedFile.objects.create(order=order, attached_file=file)
        return order
