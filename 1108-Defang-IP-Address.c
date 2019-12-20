char * defangIPaddr(char * address)
{
    int length = strlen(address);
    char *newaddress = malloc(sizeof(char) * (length * 7));
    newaddress[0] = '\0';
    for (int i = 0; i < length; i++)
    {
        if (isdigit(address[i]))
        {
            char tmp = address[i];
            strncat(newaddress, &tmp, 1);
        }
        else
        {
            char tmp[4] = "[.]";
            strcat(newaddress, tmp);
        }
    }
    return newaddress;

}
