using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ModifyTexture : MonoBehaviour
{
    public GameObject object1;

    public Material originalMaterial;

    // Start is called before the first frame update
    void Start()
    {
         if (originalMaterial == null || originalMaterial.mainTexture == null)
        {
            Debug.LogError("Original material or its main texture is missing.");
            return;
        }

        // Get the original texture from the material
        // Texture2D originalTexture = originalMaterial.mainTexture as Texture2D;
        // if (!originalTexture.isReadable)
        // {
        //     Debug.LogError("Original texture must be readable. Please enable 'Read/Write Enabled' in the texture import settings.");
        //     return;
        // }

        // // Create and apply low-resolution texture
        // Texture2D lowResTexture = CreateLowResTexture(originalTexture, 128, 128);  // Example: 128x128 resolution
        // ApplyTexture(object1, lowResTexture);

        // // Create and apply stretched texture
        // //Texture2D stretchedTexture = CreateStretchedTexture(originalTexture, 512, 256);  // Example: stretch to 512x256
        // //ApplyTexture(object2, stretchedTexture);

        // // Create and apply placeholder texture
        // //Texture2D placeholderTexture = CreatePlaceholderTexture(originalTexture.width, originalTexture.height);
        // //ApplyTexture(object3, placeholderTexture);
        Material modifiedMaterial = new Material(originalMaterial);
        //ProcessMaterialTextures(modifiedMaterial, CreateLowResTexture, 64, 64);
        //ProcessMaterialTextures(modifiedMaterial, CreatePlaceholderTexture, 128, 128);
        ProcessMaterialTextures(modifiedMaterial, CreateStretchedTexture, 1024, 16);
        Renderer renderer = object1.GetComponent<Renderer>();
        if(renderer != null)
        {
            renderer.material = modifiedMaterial;
        }
    }


    delegate Texture2D TextureProcessor(Texture2D original, int width, int height);

    void ProcessMaterialTextures(Material material, TextureProcessor processor, int width, int height)
    {
        string[] textureNames = material.GetTexturePropertyNames();

        foreach (string textureName in textureNames)
        {
            Texture2D texture = material.GetTexture(textureName) as Texture2D;
            if (texture != null && texture.isReadable)
            {
                Texture2D processedTexture = processor(texture, width, height);
                material.SetTexture(textureName, processedTexture);
            }
        }
    }
    
    Texture2D CreateLowResTexture(Texture2D original, int width, int height)
    {
        Texture2D lowResTexture = new Texture2D(width, height);
        Color[] pixels = original.GetPixels(0, 0, original.width, original.height);
        Color[] resizedPixels = new Color[width * height];

        float scaleX = (float)original.width / width;
        float scaleY = (float)original.height / height;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                // Calculate the starting position of the box filter
                int startX = (int)(x * scaleX);
                int startY = (int)(y * scaleY);

                // Calculate the number of pixels to average over
                int endX = Mathf.Min((int)((x + 1) * scaleX), original.width);
                int endY = Mathf.Min((int)((y + 1) * scaleY), original.height);

                Color avgColor = Color.black;
                int count = 0;

                // Average the colors within the box
                for (int yy = startY; yy < endY; yy++)
                {
                    for (int xx = startX; xx < endX; xx++)
                    {
                        avgColor += pixels[yy * original.width + xx];
                        count++;
                    }
                }

                // Assign the averaged color to the resized pixel
                resizedPixels[y * width + x] = avgColor / count;
            }
        }

        lowResTexture.SetPixels(resizedPixels);
        lowResTexture.Apply();
        return lowResTexture;
    }

    Texture2D CreatePlaceholderTexture(Texture2D original, int width, int height)
    {
        Texture2D placeholderTexture = new Texture2D(width, height);
        Color placeholderColor = Color.magenta;

        Color[] pixels = new Color[width * height];
        for (int i = 0; i < pixels.Length; i++)
        {
            pixels[i] = placeholderColor;
        }

        placeholderTexture.SetPixels(pixels);
        placeholderTexture.Apply();
        return placeholderTexture;
    }

    Texture2D CreateStretchedTexture(Texture2D original, int width, int height)
    {
        Texture2D stretchedTexture = new Texture2D(width, height);
        Color[] pixels = original.GetPixels(0, 0, original.width, original.height);
        Color[] stretchedPixels = new Color[width * height];

        float scaleX = (float)original.width / width;
        float scaleY = (float)original.height / height;

        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                int pixelIndex = (int)(y * scaleY) * original.width + (int)(x * scaleX);
                stretchedPixels[y * width + x] = pixels[pixelIndex];
            }
        }

        stretchedTexture.SetPixels(stretchedPixels);
        stretchedTexture.Apply();
        return stretchedTexture;
    }


    void ApplyTexture(GameObject obj, Texture2D texture)
    {
        if (obj != null)
        {
            Renderer renderer = obj.GetComponent<Renderer>();
            if (renderer != null)
            {
                Material newMaterial = new Material(renderer.material);
                newMaterial.mainTexture = texture;
                renderer.material = newMaterial;
            }
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
